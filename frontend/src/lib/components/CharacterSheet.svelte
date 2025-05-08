<script lang="ts">
  import type { Character } from "$lib/util/character";

  let { character }: { character: Character } = $props();
</script>

<article class="card">
  <header>
    <h1>{character.character_name}</h1>
  </header>
</article>

<style>
  article {
    position: absolute;
    z-index: 5;
    top: 7.75em;
  }
</style>
