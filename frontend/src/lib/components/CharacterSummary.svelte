<script lang="ts">
  import type { AbilityScores } from "$lib/util/character";

  interface Props {
    name: string;
    notes: string;
    meleeWep: string;
    rangedWep: string;
    className: string | undefined;
    classId: number | undefined;
    abilityScores: AbilityScores;
  }

  let { name, notes, meleeWep, rangedWep, className, classId, abilityScores }: Props = $props();

  function isValidAbilityScores(): boolean {
    return (abilityScores.str >= 3 && abilityScores.str <= 18)
      && (abilityScores.dex >= 3 && abilityScores.dex <= 18)
      && (abilityScores.con >= 3 && abilityScores.con <= 18)
      && (abilityScores.intl >= 3 && abilityScores.intl <= 18)
      && (abilityScores.wis >= 3 && abilityScores.wis <= 18)
      && (abilityScores.cha >= 3 && abilityScores.cha <= 18);
  }

  function isValidCharacter(): boolean {
    return isValidAbilityScores()
      && (name.length > 0)
      && (meleeWep.length > 0)
      && (rangedWep.length > 0)
      && className !== undefined;
  }
</script>

<article class="card">
  <header>
    <h4>Character Summary</h4>
  </header>
  <p>
    <strong>Name:</strong>
    {#if name.length > 0}
      {name}
    {:else}
      <span>Missing input</span>
    {/if}
  </p>
  <p>
    <strong>Melee Weapon:</strong>
    {#if meleeWep.length > 0}
      {meleeWep}
    {:else}
      <span>Missing input</span>
    {/if}
  </p>
  <p>
    <strong>Ranged Weapon:</strong>
    {#if rangedWep.length > 0}
      {rangedWep}
    {:else}
      <span>Missing input</span>
    {/if}
  </p>
  <p>
    <strong>Class:</strong>
    {#if className}
      {className}
    {:else}
      <span>Missing selection</span>
    {/if}
  </p>
  <p>
    <strong>Ability Scores:</strong>
    {#if !isValidAbilityScores()}
      <span>Missing or invalid input</span>
    {/if}
  </p>
  <div class="ability-scores">
    <div>
      <p>
        <strong>STR:</strong>
        {#if abilityScores.str >= 3 && abilityScores.str <= 18}
          {abilityScores.str}
        {:else}
          <span>-</span>
        {/if}
      </p>
      <p>
        <strong>DEX:</strong>
        {#if abilityScores.dex >= 3 && abilityScores.dex <= 18}
          {abilityScores.dex}
        {:else}
          <span>-</span>
        {/if}
      </p>
      <p>
        <strong>CON:</strong>
        {#if abilityScores.con >= 3 && abilityScores.con <= 18}
          {abilityScores.con}
        {:else}
          <span>-</span>
        {/if}
      </p>
    </div>
    <div>
      <p>
        <strong>INT:</strong>
        {#if abilityScores.intl >= 3 && abilityScores.intl <= 18}
          {abilityScores.intl}
        {:else}
          <span>-</span>
        {/if}
      </p>
      <p>
        <strong>WIS:</strong>
        {#if abilityScores.wis >= 3 && abilityScores.wis <= 18}
          {abilityScores.wis}
        {:else}
          <span>-</span>
        {/if}
      </p>
      <p>
        <strong>CHA:</strong>
        {#if abilityScores.cha >= 3 && abilityScores.cha <= 18}
          {abilityScores.cha}
        {:else}
          <span>-</span>
        {/if}
      </p>
    </div>
  </div>
</article>

{#if isValidCharacter()}
  <label for="confirm-modal" class="button below-card-content create">Create Character</label>
{:else}
  <p class="below-card-content">Please fix any missing or invalid inputs before proceeding.</p>
{/if}

<div class="modal">
  <input type="checkbox" id="confirm-modal">
  <label for="confirm-modal" class="overlay"></label>
  <article>
    <header>
      <h3>Confirm Creation</h3>
      <label for="confirm-modal" class="close">&times;</label>
    </header>
    <form method="POST" action="/character-creation">
      <input type="hidden" name="class-id" value={classId}>
      <input type="hidden" name="char-name" value={name}>
      <input type="hidden" name="ability-scores" value={abilityScores}>
      <input type="hidden" name="bkg-notes" value={notes}>
      <input type="hidden" name="melee-wep" value={meleeWep}>
      <input type="hidden" name="ranged-wep" value={rangedWep}>
      <section class="content">
        If you would like to make any changes to your character, you may go 
        back and edit your responses. If you're ready to go, hit create!
      </section>
      <footer class="confirm-buttons">
        <div class="back-button">
          <label for="confirm-modal" class="button">Go Back</label>
        </div>
        <div class="create-button">
          <input type="submit" class="button success" value="Create">
        </div>
      </footer>
    </form>
  </article>
</div>

<style>
  article {
    width: 20em;
    margin: auto;
    font-size: 0.9em;
  }

  header {
    display: flex;
    align-items: center;
  }

  span {
    color: red;
  }

  .ability-scores {
    display: grid;
    justify-content: center;
    margin: auto;
    grid-template-columns: auto auto;
    width: 10em;
    margin-bottom: 1em;
    column-gap: 2em;
  }

  .ability-scores div {
    width: 5em;
  }

  .below-card-content {
    margin: auto;
    margin-top: 1em;
    width: 15em;
  }

  .create {
    width: 10em;
  }

  .confirm-buttons {
    display: grid;
    grid-template-columns: auto auto;
  }

  .create-button {
    display: flex;
    justify-content: end;
  }
</style>
