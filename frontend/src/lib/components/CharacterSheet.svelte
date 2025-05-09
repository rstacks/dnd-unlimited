<script lang="ts">
  import type { Character } from "$lib/util/character";
  import Overview from "./character-sheet/Overview.svelte";

  interface Props {
    character: Character;
    xpGoal: number;
    show: boolean;
  }

  let { character, xpGoal, show=$bindable() }: Props = $props();
  let sheetTab: "overview" | "weapons" | "skillsAndSaves" | "spells" | "stats"  = $state("overview");
</script>

<div class="character-sheet">
  <article class="card">
    <header>
      <div class="close-button">
        <button class="pseudo" onclick="{() => {show = false}}">
          <img src="back-icon.svg" alt="Back to Characters View Button">
        </button>
      </div>
      <img class="class-icon" src="{"class-icons/" + character.class_name.toLowerCase() + ".svg"}"
        alt="{character.class_name + " class icon"}">
      <div class="content">
        <h3>{character.character_name}</h3>
        <p>Level {character.lvl} {character.class_name}</p>
        <input class="xp-input" type="number" autocomplete="off"
          value={character.xp}>
        <span>/{xpGoal} XP</span>
      </div>
    </header>
    <section class="sheet-content">
      {#if sheetTab === "overview"}
        <Overview hit_dice={character.hit_dice}
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
        <div>
          shit
        </div>
      {:else if sheetTab === "skillsAndSaves"}
        <div>
          balls
        </div>
      {:else if sheetTab === "spells"}
        <div>
          cock
        </div>
      {:else if sheetTab === "stats"}
        <div>
          damn
        </div>
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
        <span>Spells</span>
      </button>
      <button onclick="{() => {sheetTab = "stats"}}"
        style:background-color="{sheetTab === "stats" ? "rgb(219, 219, 219)" : "white"}">
        <img src="character-sheet-icons/stats.svg" alt="Stats Icon">
        <span>Stats</span>
      </button>
    </footer>
  </article>
</div>

<style>
  .character-sheet {
    position: absolute;
    z-index: 5;
    top: 8.5em;
    left: 0.2em;
    right: 0.2em;
    /* height: 100%; */
  }

  article {
    max-width: 60em;
    margin: auto;
    /* height: 100%; */
  }

  header {
    display: flex;
    align-items: center;
    position: absolute;
    top: 0;
    background-color: white;
    width: 100%;
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
    margin: 0;
    padding: 0;
    overflow: auto;
    /* height: 100%; */
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
    position: absolute;
    bottom: 0;
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
  }

  .character-sheet-tab-buttons img {
    width: 3em;
  }

  .xp-input {
    width: 6em;
  }
</style>
