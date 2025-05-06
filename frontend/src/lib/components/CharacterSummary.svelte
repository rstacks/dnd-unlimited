<script lang="ts">
  import type { AbilityScores } from "$lib/util/character";

  interface Props {
    name: string;
    meleeWep: string;
    rangedWep: string;
    className: string | undefined;
    abilityScores: AbilityScores;
  }

  let { name, meleeWep, rangedWep, className, abilityScores }: Props = $props();
</script>

<article class="card">
  <header>
    <h4>Character Summary</h4>
  </header>
  <p>
    <strong>Name:</strong>
    {#if name}
      {name}
    {/if}
  </p>
  <p><strong>Melee Weapon:</strong> {meleeWep}</p>
  <p><strong>Ranged Weapon:</strong> {rangedWep}</p>
  <p><strong>Class:</strong> {className}</p>
  <p><strong>Ability Scores:</strong></p>
  <div class="ability-scores">
    <div>
      <p><strong>STR:</strong> {abilityScores.str}</p>
      <p><strong>DEX:</strong> {abilityScores.dex}</p>
      <p><strong>CON:</strong> {abilityScores.con}</p>
    </div>
    <div>
      <p><strong>INT:</strong> {abilityScores.intl}</p>
      <p><strong>WIS:</strong> {abilityScores.wis}</p>
      <p><strong>CHA:</strong> {abilityScores.cha}</p>
    </div>
  </div>
</article>

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
</style>
