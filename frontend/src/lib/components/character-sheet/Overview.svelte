<script lang="ts">
  import { getAbilityModifier } from "$lib/util/character-functions";

  interface Props {
    char_id: number;
    hit_dice: string;
    lvl: number;
    dex: number;
    armor_class: number;
    hp: number;
    max_hp: number;
    notes: string;
    status_effects: string;
    proficiency_bonus: number;
    speed: number;
  }

  let props: Props = $props();

  function updateNotes(): void {
    const notesInput = document.getElementById("bkg-info-input") as HTMLInputElement;
    const notes = notesInput.value;
    try {
      localStorage.setItem(props.char_id + "-notes", notes);
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getNotes(): string {
    const notes = localStorage.getItem(props.char_id + "-notes");
    if (!notes) {
      return props.notes;
    }
    return notes;
  }

  function updateHp(): void {
    const hpInput = document.getElementById("hp-input") as HTMLInputElement;
    const hp = hpInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-hp", hp.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getHp(): number {
    const hp = localStorage.getItem(props.char_id + "-hp");
    if (!hp) {
      return props.hp;
    }
    return Number(hp);
  }
</script>

<div class="bkg-info">
  <strong>Background Info</strong>
  <textarea placeholder="Background Info (Optional)" value={getNotes()}
    id="bkg-info-input" onchange="{() => {updateNotes()}}"></textarea>
</div>
<div class="combat-info">
  <div class="not-hp">
    <div>
      <strong>Initiative</strong>
      <span>
        {#if getAbilityModifier(props.dex) >= 0}
          +{getAbilityModifier(props.dex)}
        {:else}
          {getAbilityModifier(props.dex)}
        {/if}
      </span>
    </div>
  
    <div>
      <strong>Hit Dice</strong>
      <span>{props.lvl}{props.hit_dice}</span>
    </div>
  
    <div>
      <strong>Armor Class</strong>
      <span>{props.armor_class}</span>
    </div>
  </div>

  <div class="hp-info">
    <strong>Hit Points</strong>
    <fieldset class="hp-display">
      <input class="numeric-input" type="number" autocomplete="off"
        value={getHp()} id="hp-input" onchange="{() => {updateHp()}}">
      <span>
        / {props.max_hp} HP
      </span>
    </fieldset>
  </div>
</div>
<div class="stat-info">
  <div>
    <strong>Proficiency Bonus</strong>
    <span>+{props.proficiency_bonus}</span>
  </div>
  <div>
    <strong>Speed</strong>
    <span>{props.speed} ft</span>
  </div>
</div>
<div class="bkg-info status">
  <strong>Status Effects</strong>
  {#if !props.status_effects}
    <p>No active effects</p>
  {:else}
    <p>
      {#each props.status_effects as chr}
        {#if chr === "\n"}<br><br>{:else}{chr}{/if}
      {/each}
    </p>
  {/if}
</div>

<style>
  textarea {
    resize: vertical;
  }

  .numeric-input {
    width: 6em;
    margin-right: 0.25em;
  }

  .bkg-info {
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    width: 19em;
    margin: auto;
    margin-top: 1em;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  .combat-info {
    display: flex;
    flex-direction: column;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    margin: auto;
    margin-top: 1em;
    width: 19em;
  }

  .not-hp {
    display: flex;
    justify-content: center;
  }

  .not-hp div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-left: 0.25em;
    margin-right: 0.25em;
    text-align: center;
    background-color: rgb(196, 230, 242);
    padding: 0.5em;
    border-radius: 0.5em;
  }

  .hp-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: rgb(196, 230, 242);
    width: fit-content;
    padding: 0.5em;
    margin: auto;
    border-radius: 0.5em;
    margin-top: 0.5em;
  }

  .stat-info {
    display: flex;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    justify-content: center;
    width: 19em;
    margin: auto;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    margin-top: 1em;
  }
  
  .stat-info div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-left: 0.75em;
    margin-right: 0.75em;
    text-align: center;
    background-color: rgb(196, 230, 242);
    padding: 0.5em;
    border-radius: 0.5em;
  }

  .status {
    margin-top: 1em;
    margin-bottom: 1em;
  }

  fieldset.hp-display {
    display: flex;
    align-items: center;
  }
</style>
