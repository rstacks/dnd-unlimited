<script lang="ts">
  import type { Character } from "$lib/util/character";
  import CharacterSheet from "./CharacterSheet.svelte";

  export const LEVEL_TO_XP_MIN = {
    1: 0,
    2: 300,
    3: 900,
    4: 2700,
    5: 6500,
    6: 14000,
    7: 23000,
    8: 34000,
    9: 48000,
    10: 64000,
    11: 85000,
    12: 100000,
    13: 120000,
    14: 140000,
    15: 165000,
    16: 195000,
    17: 225000,
    18: 265000,
    19: 305000,
    20: 355000
  };

  let { character }: { character: Character } = $props();
  let nextLevel = Number(character.lvl) + 1;
  let nextLevelKey = $state(nextLevel as keyof typeof LEVEL_TO_XP_MIN);
  let showCharacterSheet = $state(false);
</script>

<article class="card">
  <img class="class-icon" src="{"class-icons/" + character.class_name.toLowerCase() + ".svg"}"
    alt="{character.class_name + " class icon"}">
  <div class="content">
    <h3>{character.character_name}</h3>
    <p>Level {character.lvl} {character.class_name}</p>
    <span>{character.xp}/{LEVEL_TO_XP_MIN[nextLevelKey]} XP</span>
  </div>
  <div class="select-class-button">
    <button class="pseudo" onclick="{() => {showCharacterSheet = true}}">
      <img src="start-icon.svg" alt="Choose This Character Button">
    </button>
  </div>
</article>

{#if showCharacterSheet}
  <CharacterSheet character={character}
    xpGoal={LEVEL_TO_XP_MIN[nextLevelKey]}
    bind:show={showCharacterSheet} />
{/if}

<style>
  article {
    display: flex;
    align-items: center;
    max-width: 25em;
    margin: auto;
    margin-bottom: 1em;
  }

  .class-icon {
    width: 5em;
    margin: 1em;
  }

  h3 {
    padding: 0;
  }

  .content {
    padding-top: 1em;
    padding-bottom: 1em;
  }

  button {
    display: flex;
    padding: 0.2em;
    margin-right: 1em;
  }

  button img {
    width: 1.5em;
  }

  .select-class-button {
    display: flex;
    flex-grow: 1;
    align-items: center;
    justify-content: end;
  }
</style>
