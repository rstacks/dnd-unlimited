<svelte:head>
  <title>App Unavailable | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
  import { page } from "$app/state";
</script>

<Title />

<p class="card">
  It appears your dungeon master is offline, adventurer. They shall return
  soon. In the meantime, safe travels!
</p>

<p class="card centered"><strong>{page.status} {page.error?.message}</strong></p>

<style>
  p {
    max-width: 50em;
    width: 80%;
    padding: 1em;
    margin: auto;
    margin-top: 1em;
  }

  p.centered {
    text-align: center;
    width: fit-content
  }
</style>
