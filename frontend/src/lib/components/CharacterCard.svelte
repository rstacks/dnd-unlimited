<script lang="ts">
  import type { Character, Skill } from "$lib/util/character";
  import CharacterSheet from "./CharacterSheet.svelte";
  import { LEVEL_TO_XP_MIN } from "$lib/util/character-functions";

  interface Props {
    character: Character;
    hideDashboard: boolean;
    skills: Skill[];
    showLoading: boolean;
  }

  let { character, hideDashboard=$bindable(), skills, showLoading=$bindable() }: Props = $props();
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
    <button class="pseudo" onclick="{() => {
        showCharacterSheet = true;
        hideDashboard = true;
      }}">
      <img src="start-icon.svg" alt="Choose This Character Button">
    </button>
  </div>
</article>

{#if showCharacterSheet}
  <CharacterSheet character={character}
    xpGoal={LEVEL_TO_XP_MIN[nextLevelKey]}
    bind:show={showCharacterSheet}
    bind:hideDash={hideDashboard}
    skills={skills}
    bind:showLoading={showLoading} />
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
