<script lang="ts">
  import type { Spell } from "$lib/util/spell";

  let { spell }: { spell: Spell } = $props();

  let showMore = $state(false);

  function toggleShowMore(): void {
    showMore = !showMore;
  }

  function capitalize(str: string): string {
    return str.at(0)?.toUpperCase() + str.substring(1);
  }
</script>

<article class="card" style:padding-bottom="{showMore ? "1em" : "0"}">
  <header>
    <div class="spell-name">
      <h4><i>{capitalize(spell.spell_type)}</i> {spell.spell_name}</h4>
    </div>
    <div class="show-icon">
      <button class="pseudo" onclick="{() => {toggleShowMore()}}">
        {#if showMore}
          <img src="updown-icon.svg" alt="Less Spell Info Button">
        {:else}
          <img src="dropdown-icon.svg" alt="More Spell Info Button">
        {/if}
      </button>
    </div>
  </header>
  {#if showMore}
    <section>
      <span>
        {#each spell.spell_desc as chr}
          {#if chr === "\n"}<br><br>{:else if chr === "*"}&#x2022;{:else}{chr}{/if}
        {/each}
      </span>
    </section>
  {/if}
</article>

<style>
  article {
    margin: auto;
    margin-bottom: 1em;
  }

  header {
    display: grid;
    grid-template-columns: auto auto;
    padding: 0;
    padding-left: 1em;
    padding-right: 1em;
  }

  button {
    display: flex;
    padding: 0.25em;
  }

  .spell-name {
    display: flex;
    align-items: center;
  }

  .show-icon {
    display: flex;
    justify-content: end;
  }

  section {
    padding: 1em;
  }
</style>
