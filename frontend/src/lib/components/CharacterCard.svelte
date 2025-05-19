<script lang="ts">
  import type { Character, Skill } from "$lib/util/character";
  import CharacterSheet from "./CharacterSheet.svelte";
  import { LEVEL_TO_XP_MIN } from "$lib/util/character-functions";
  import { closeModal } from "$lib/util/util";

  interface Props {
    characterList: Character[];
    character: Character;
    hideDashboard: boolean;
    skills: Skill[];
    showLoading: boolean;
  }

  let { characterList, character, hideDashboard=$bindable(), skills, showLoading=$bindable() }: Props = $props();
  let nextLevel = Number(character.lvl) + 1;
  let nextLevelKey = $state(nextLevel as keyof typeof LEVEL_TO_XP_MIN);
  let showCharacterSheet = $state(false);
</script>

<article class="card character-card">
  <div>
    <label class="trash pseudo button" for="{"delete-modal-" + character.id}">
      <img src="trash-icon.svg" alt="Delete Character Button">
    </label>
  </div>
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

{#each characterList as char}
  <div class="modal">
    <input type="checkbox" id="{"delete-modal-" + char.id}">
    <label for="{"delete-modal-" + char.id}" class="overlay"></label>
    <article>
      <header>
        <h3>Delete Character</h3>
        <label for="{"delete-modal-" + char.id}" class="close">&times;</label>
      </header>
      <form method="POST" action="/dashboard?/deleteCharacter">
        <input type="hidden" name="char-id" value={char.id}>
        <section class="content">
          Are you sure you want to delete this character?
        </section>
        <footer>
          <label for="{"delete-modal-" + char.id}" class="button">Cancel</label>
          <input type="submit" value="Delete" class="dangerous"
            onclick="{() => {
              closeModal("delete-modal-" + char.id);
              showLoading = true;
            }}">
        </footer>
      </form>
    </article>
  </div>
{/each}

{#if showCharacterSheet}
  <CharacterSheet character={character}
    xpGoal={LEVEL_TO_XP_MIN[nextLevelKey]}
    bind:show={showCharacterSheet}
    bind:hideDash={hideDashboard}
    skills={skills}
    bind:showLoading={showLoading} />
{/if}

<style>
  article.character-card {
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

  div.content {
    padding-top: 1em;
    padding-bottom: 1em;
  }

  @media (max-width: 450px) {
    article.character-card {
      font-size: 0.85em;
    }
  }

  button {
    display: flex;
    padding: 0.2em;
    margin-left: 1em;
    margin-right: 1em;
  }

  label.trash {
    display: flex;
    padding: 0.2em;
    margin-left: 1em;
    margin-right: 0;
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
