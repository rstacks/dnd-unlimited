<script lang="ts">
  let showMore = $state(false);

  function toggleShowMore() {
    showMore = !showMore;
  }
</script>

<article class="card">
  <header>
    <div class="spell-name">
      <h4><i>Casted</i> Dissonant Whispers</h4>
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
      <span>One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes 3d6 damage and must immediately move as far away from you as it can, using the safest route. On a successful save, the target takes half as much damage only.\nThe damage increases by 1d6 for each spell slot level above 1.</span>
    </section>
  {/if}
</article>

<style>
  article {
    max-width: 20em;
    margin: auto;
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
    font-size: 0.75em;
    padding: 1em;
  }
</style>
