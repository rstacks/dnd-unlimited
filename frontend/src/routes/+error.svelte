<svelte:head>
  <title>App Offline | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
  import { page } from "$app/state";
</script>

<Title />

<article class="card">
  <div>
    <p>
      It appears your dungeon master is offline, adventurer. They shall return
      soon. If your dungeon master is actually online, hit the button below to reconnect.
      Otherwise, safe travels!
    </p>
  </div>
  <a href="/dashboard" class="button">Retry</a>
</article>

<p class="card centered"><strong>{page.status} {page.error?.message}</strong></p>

<style>
  article {
    margin-top: 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: left;
    max-width: 30em;
    width: 80%;
    margin: auto;
    padding: 1em;
  }

  p.centered {
    text-align: center;
    width: fit-content;
    padding: 0.5em;
    margin: auto;
    margin-top: 1em;
  }

  a {
    width: fit-content;
    margin: auto;
    margin-top: 1em;
  }
</style>
