<svelte:head>
  <title>Dashboard | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import TitleBar from "$lib/components/TitleBar.svelte";
  import CharacterCard from "$lib/components/CharacterCard.svelte";
  import Loading from "$lib/components/Loading.svelte";
  import { beforeNavigate } from "$app/navigation";
  import { onMount } from "svelte";
  import { closeModal, isIosBrowser } from "$lib/util/util";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();
  let showCharacterSheetStates: boolean[] = $state(data.charSheetStates);
  let showDashboard: boolean = $derived(showCharacterSheetStates.findIndex((elem) => elem) === -1);
  let showLoading = $state(false);

  onMount(() => {
    if (isIosBrowser()) {
      window.location.replace("/install");
    }
  });

  beforeNavigate(() => { showLoading = true });
</script>

{#if showLoading}
  <Loading />
{/if}

{#if showDashboard}
  <TitleBar account_modal_class="my-modal" />
{/if}

<div class="scrollable-area" style={showDashboard ? "" : "height: 0; overflow: hidden;"}>
  <div class="spacer"></div>

  <article class="card welcome">
    <header>
      <h2>Greetings, {data.name}</h2>
    </header>
  </article>
  
  {#if data.characters.length === 0}
    <p class="no-characters">You don't have any characters. Why not create one?</p>
  {:else}
    <div class="character-cards">
      {#each data.characters as character, i}
        <CharacterCard characterList={data.characters}
          character={character}
          bind:hideDashboard={showCharacterSheetStates[i]}
          skills={data.skills}
          bind:showLoading={showLoading} />
      {/each}
    </div>
  {/if}
  
  <div class="new-character-button">
    <a class="add button" href="/character-creation"
      onclick="{() => { showLoading = true }}">
      <img src="add-icon.svg" alt="Add Character Button">
      <span>New Character</span>
    </a>
  </div>
</div>

<div class="modal">
  <input type="checkbox" id="my-modal">
  <label for="my-modal" class="overlay"></label>
  <article>
    <header>
      <h3>Account</h3>
      <label for="my-modal" class="close">&times;</label>
    </header>
    <form method="POST" action="?/updateName">
      <section class="content">
        <label for="user-name" class="name-label">Name:</label>
        <input type="text" name="user-name" placeholder="Name"
          autocomplete="off" value="{data.name}" class="name-input">
      </section>
      <footer class="flex">
        <div class="save-button">
          <input type="submit" value="Save" onclick="{() => {
              closeModal("my-modal");
              showLoading = true;
            }}">
        </div>
        <div class="logout-button">
          <input type="submit" value="Log Out" class="error"
            formaction="?/logout" onclick="{() => {
              closeModal("my-modal");
              showLoading = true;
            }}">
        </div>
      </footer>
    </form>
  </article>
</div>

<style>
  .spacer {
    height: 5em;
  }

  .welcome {
    width: fit-content;
    margin: auto;
    font-size: 0.75em;
    margin-bottom: 2em;
  }

  .welcome header {
    display: flex;
    text-align: center;
  }

  .welcome h2 {
    margin: 0;
  }

  .name-input {
    width: 70%;
  }

  .name-label:hover {
    cursor: default;
  }

  footer {
    padding: 0;
  }

  .save-button {
    margin-left: 1em;
    padding: 0;
  }

  .logout-button {
    display: flex;
    justify-content: end;
    margin-right: 0.4em;
    padding: 0;
  }

  .no-characters {
    text-align: center;
    width: 25em;
    margin: auto;
    font-size: 0.75em;
    color: rgb(99, 102, 109);
    margin-bottom: 1em;
    margin-top: 2em;
  }

  .add {
    display: flex;
    width: fit-content;
    padding: 0.25em;
    border-radius: 1em;
    margin: auto;
  }

  .add span {
    margin-left: 0.25em;
    margin-right: 0.5em;
  }

  .character-cards {
    margin-left: 0.5em;
    margin-right: 0.5em;
  }

  .new-character-button {
    padding-bottom: 3em;
  }
</style>
