<script lang="ts">
  import type { Spell } from "$lib/util/spell";
  import SpellCard from "../SpellCard.svelte";

  let { spells }: { spells: Spell[] } = $props();
</script>

<div class="spells">
  <strong>Spells</strong>
  <div class="spell-cards">
    {#each spells as spell}
      <SpellCard spell={spell} />
    {/each}
  </div>
</div>

<style>
  div.spells {
    width: 19em;
    margin: auto;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  div.spell-cards {
    margin-top: 0.5em;
    font-size: 0.75em;
  }
</style>
