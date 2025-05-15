<script lang="ts">
  import type { Character, Skill } from "$lib/util/character";
  import Overview from "./character-sheet/Overview.svelte";
  import Weapons from "./character-sheet/Weapons.svelte";
  import SkillsAndSaves from "./character-sheet/SkillsAndSaves.svelte";
  import Spells from "./character-sheet/Spells.svelte";
  import AbilityScores from "./character-sheet/AbilityScores.svelte";
  import { LEVEL_TO_XP_MIN } from "$lib/util/character-functions";
  import { applyAction, enhance } from "$app/forms";
  import { invalidateAll } from "$app/navigation";
  import { closeModal } from "$lib/util/util";

  interface Props {
    character: Character;
    xpGoal: number;
    show: boolean;
    hideDash: boolean;
    skills: Skill[];
    showLoading: boolean;
  }

  let {
    character,
    xpGoal,
    show=$bindable(),
    hideDash=$bindable(),
    skills,
    showLoading=$bindable()
  }: Props = $props();
  let sheetTab: "overview" | "weapons" | "skillsAndSaves" | "spells" | "stats"  = $state("overview");
  let abilitiesToUpgrade = $state("");
  let numAbilitiesToUpgrade = $state(0);

  function isAbilityScoreIncreaseTime(lvl: number): boolean {
    if (lvl % 4 === 0 && lvl < 20) {
      return true;
    }
    return false;
  }

  function setAbilitiesToUpgrade(abilityName: string): void {
    if (abilitiesToUpgrade.includes(abilityName)) {
      abilitiesToUpgrade = abilitiesToUpgrade.replace(abilityName, "");
      numAbilitiesToUpgrade--;
    } else {
      abilitiesToUpgrade += " " + abilityName;
      numAbilitiesToUpgrade++;
    }
  }

  function updateXp(): void {
    const xpInput = document.getElementById("experience-input") as HTMLInputElement;
    const xp = xpInput.valueAsNumber;

    const currentLvl = character.lvl as keyof typeof LEVEL_TO_XP_MIN;
    if (xp < LEVEL_TO_XP_MIN[currentLvl]) {
      return;
    }

    try {
      localStorage.setItem(character.id + "-xp", xp.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }

  function refreshSheet(): void {
    const form = document.getElementById("char-sheet-form") as HTMLFormElement;
    const formInputs = form.getElementsByTagName("input");

    const xpVal = localStorage.getItem(character.id + "-xp");
    localStorage.removeItem(character.id + "-xp");
    const notesVal = localStorage.getItem(character.id + "-notes");
    localStorage.removeItem(character.id + "-notes");
    const hpVal = localStorage.getItem(character.id + "-hp");
    localStorage.removeItem(character.id + "-hp");

    let xpInput = formInputs.item(1)
    let notesInput = formInputs.item(2)
    let hpInput = formInputs.item(3)
    
    if (xpVal && !Number.isNaN(Number(xpVal))) {
      xpInput!.value = xpVal;
    }
    if (notesVal) {
      notesInput!.value = notesVal;
    }
    if (hpVal && !Number.isNaN(Number(hpVal))) {
      hpInput!.value = hpVal;
    }

    form.requestSubmit();
  }

  function isIosBrowser(): boolean {
    /**
     * Type "any" because standalone property only exists on Safari iOS.
     * TS does not recognize it as a standard property.
     */
    const navigator: any = window.navigator;
    if (navigator.standalone !== undefined && !(navigator.standalone)) {
      return true;
    }
    return false;
  }
</script>

<div class="character-sheet">
  <article class="card {isIosBrowser() ? "ios-browser" : ""}">
    <header>
      <div class="close-button">
        <button class="pseudo" onclick="{() => {
            show = false;
            hideDash = false;
            refreshSheet();
          }}">
          <img src="back-icon.svg" alt="Back to Characters View Button">
        </button>
      </div>
      <img class="class-icon" src="{"class-icons/" + character.class_name.toLowerCase() + ".svg"}"
        alt="{character.class_name + " class icon"}">
      <div class="content">
        <h3>{character.character_name}</h3>
        <p>Level {character.lvl} {character.class_name}</p>
        {#if character.xp >= xpGoal}
          <label for="level-up-modal" class="button">Level Up</label>
        {:else}
          <div class="xp-progress">
            <input class="xp-input" type="number" autocomplete="off"
              value={character.xp} id="experience-input" onchange="{() => {updateXp()}}">
            <span>/{xpGoal} XP</span>
          </div>
        {/if}
      </div>
      <div class="refresh-button">
        <button class="pseudo" onclick="{() => {refreshSheet()}}">
          <img src="refresh-icon.svg" alt="Refresh Character Button">
        </button>
      </div>
    </header>
    <section class="sheet-content">
      {#if sheetTab === "overview"}
        <Overview char_id={character.id}
          hit_dice={character.hit_dice}
          lvl={character.lvl}
          dex={character.dex}
          armor_class={character.armor_class}
          hp={character.hp}
          max_hp={character.max_hp}
          notes={character.notes}
          status_effects={character.status_effects}
          proficiency_bonus={character.proficiency_bonus}
          speed={character.speed} />
      {:else if sheetTab === "weapons"} 
        <Weapons str={character.str}
          dex={character.dex}
          weapons={character.weapons}
          items={character.items} />
      {:else if sheetTab === "skillsAndSaves"}
        <SkillsAndSaves skills={skills}
          str={character.str}
          dex={character.dex}
          con={character.con}
          intl={character.intl}
          wis={character.wis}
          cha={character.cha}
          proficiency_bonus={character.proficiency_bonus}
          charSaves={character.saves}
          charSkills={character.skills} />
      {:else if sheetTab === "spells"}
        <Spells char_id={character.id}
          spells={character.spells}
          feat_name={character.feat_name}
          feat_desc={character.feat_desc}
          lvl_1_spell_slots={character.lvl_1_spell_slots}
          lvl_2_spell_slots={character.lvl_2_spell_slots}
          lvl_3_spell_slots={character.lvl_3_spell_slots}
          lvl_4_spell_slots={character.lvl_4_spell_slots}
          rages={character.rages}
          rage_damage={character.rage_damage}
          second_wind={character.second_wind}
          martial_arts={character.martial_arts}
          sneak_attack={character.sneak_attack} />
      {:else if sheetTab === "stats"}
        <AbilityScores str={character.str}
          dex={character.dex}
          con={character.con}
          intl={character.intl}
          wis={character.wis}
          cha={character.cha} />
      {/if}
    </section>
    <footer class="character-sheet-tab-buttons">
      <button onclick="{() => {sheetTab = "overview"}}"
        style:background-color="{sheetTab === "overview" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/overview.svg" alt="Overview Icon">
        <span>Overview</span>
      </button>
      <button onclick="{() => {sheetTab = "weapons"}}"
        style:background-color="{sheetTab === "weapons" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/weapons.svg" alt="Weapons and Items Icon">
        <span>Weapons & Items</span>
      </button>
      <button onclick="{() => {sheetTab = "skillsAndSaves"}}"
        style:background-color="{sheetTab === "skillsAndSaves" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/skills.svg" alt="Skills and Saves Icon">
        <span>Skills & Saves</span>
      </button>
      <button onclick="{() => {sheetTab = "spells"}}"
        style:background-color="{sheetTab === "spells" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/spells.svg" alt="Spells and Feats Icon">
        {#if character.feat_name === "Spellcasting"}
          <span>Spells</span>
        {:else}
          <span>Feat</span>
        {/if}
      </button>
      <button onclick="{() => {sheetTab = "stats"}}"
        style:background-color="{sheetTab === "stats" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/stats.svg" alt="Stats Icon">
        <span>Ability Scores</span>
      </button>
    </footer>
  </article>
</div>

<form style:display="none" method="POST" action="/dashboard?/updateCharacter"
  id="char-sheet-form" use:enhance={() => {
    showLoading = true;
    
    return async ({ result }) => {
      await applyAction(result);
      await invalidateAll();
      showLoading = false;
    };
  }}>
  <input type="hidden" name="char-id" value={character.id}>
  <input type="hidden" name="xp" value={character.xp}>
  <input type="hidden" name="notes" value={character.notes}>
  <input type="hidden" name="hp" value={character.hp}>
</form>

<div class="modal">
  <input type="checkbox" id="level-up-modal">
  <label for="level-up-modal" class="overlay"></label>
  <article class="level-up">
    <header>
      <h3>Level Up</h3>
      <label for="level-up-modal" class="close">&times;</label>
    </header>
    <form method="POST" action="/dashboard?/levelUp">
      <input type="hidden" name="char-id" value={character.id}>
      <input type="hidden" name="next-lvl" value={Number(character.lvl) + 1}>
      <input type="hidden" name="class-id" value={character.class_id}>
      <input type="hidden" name="ability-scores" value={abilitiesToUpgrade}>
      <input type="hidden" name="num-ability-scores" value={numAbilitiesToUpgrade}>
      <input type="hidden" name="hit-die" value={character.hit_dice}>
      <input type="hidden" name="con" value={character.con}>
      <section class="content ability-score-checkboxes">
        {#if isAbilityScoreIncreaseTime(Number(character.lvl) + 1)}
          <p>
            Select one ability score to increase by 2 OR two ability scores
            to increase by 1. Then, hit the button below to level up!
          </p>
          <div class="label-centerer">
            <div class="labels">
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("str")}}"
                  disabled={character.str >= 20}>
                <span class="checkable">Strength (Current Score: {character.str})</span>
              </label>
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("dex")}}"
                  disabled={character.dex >= 20}>
                <span class="checkable">Dexterity (Current Score: {character.dex})</span>
              </label>
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("con")}}"
                  disabled={character.con >= 20}>
                <span class="checkable">Constitution (Current Score: {character.con})</span>
              </label>
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("intl")}}"
                  disabled={character.intl >= 20}>
                <span class="checkable">Intelligence (Current Score: {character.intl})</span>
              </label>
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("wis")}}"
                  disabled={character.wis >= 20}>
                <span class="checkable">Wisdom (Current Score: {character.wis})</span>
              </label>
              <label>
                <input type="checkbox" oninput="{() => {setAbilitiesToUpgrade("cha")}}"
                  disabled={character.cha >= 20}>
                <span class="checkable">Charisma (Current Score: {character.cha})</span>
              </label>
            </div>
          </div>
        {:else}
          <p>Hit the button below to level up!</p>
        {/if}
      </section>
      <footer class="level-up">
        {#if isAbilityScoreIncreaseTime(Number(character.lvl) + 1)
            && (numAbilitiesToUpgrade >= 1 && numAbilitiesToUpgrade <= 2)}
          <input type="submit" class="button success" value="Level Up"
            onclick="{() => {
              closeModal("level-up-modal");
              showLoading = true;
            }}">
        {:else if !isAbilityScoreIncreaseTime(Number(character.lvl) + 1)}
          <input type="submit" class="button success" value="Level Up"
            onclick="{() => {
              closeModal("level-up-modal");
              showLoading = true;
            }}">
        {/if}
      </footer>
    </form>
  </article>
</div>

<style>
  .character-sheet {
    position: absolute;
    z-index: 5;
    top: 0;
    left: 0;
    width: 100%;
    height: fit-content;
    background-color: rgb(175, 196, 255);
    touch-action: none;
  }

  article {
    max-width: 30em;
    width: 100%;
    margin: auto;
    height: 100vh;
    display: grid;
    grid-template-rows: 2fr 70fr 1fr;
  }

  article.ios-browser {
    height: 95vh;
  }

  header {
    display: flex;
    align-items: center;
    background-color: white;
    width: 100%;
  }

  .class-icon {
    margin-right: 0.5em;
  }

  .class-icon {
    width: 5em;
  }

  .close-button button {
    display: flex;
    padding: 0.1em;
  }

  .close-button button img {
    width: 1.5em;
  }

  .sheet-content {
    display: block;
    padding: 0;
    overflow: auto;
  }

  .character-sheet-tab-buttons {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    border-style: solid;
    border-color: rgb(168, 168, 168);
    border-width: 0.1em;
    border-bottom: 0;
    border-left: 0;
    border-right: 0;
    font-size: 0.5em;
    padding: 0;
  }

  @media (max-width: 500px) {
    .character-sheet-tab-buttons {
      font-size: 0.45em;
    }
  }

  .character-sheet-tab-buttons button {
    height: 100%;
    padding: 0.25em;
    margin: 0;
    border-radius: 0;
    background-color: transparent;
    color: black;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-bottom: 5em;
  }

  .character-sheet-tab-buttons img {
    width: 3em;
  }

  .xp-input {
    width: 6em;
    margin-right: 0.25em;
  }

  .refresh-button {
    flex-grow: 1;
    display: flex;
    justify-content: end;
  }

  .refresh-button button {
    display: flex;
    padding: 0.1em;
  }

  .refresh-button button img {
    width: 1.5em;
  }

  footer.level-up {
    display: flex;
    justify-content: center;
  }

  article.level-up {
    height: fit-content;
  }

  .ability-score-checkboxes .labels {
    display: flex;
    flex-direction: column;
    align-items: left;
  }

  div.label-centerer {
    width: fit-content;
    margin: auto;
  }

  div.xp-progress {
    font-size: 0.9em;
    display: flex;
    align-items: center;
  }
</style>
