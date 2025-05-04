<svelte:head>
  <title>Dashboard | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import TitleBar from "$lib/components/TitleBar.svelte";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();
</script>

<TitleBar account_modal_class="my-modal" />

<div class="spacer"></div>

<article class="card welcome">
  <header>
    <h2>Welcome, {data.name}!</h2>
  </header>
</article>

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
          <input type="submit" value="Save">
        </div>
        <div class="logout-button">
          <input type="submit" value="Log Out" class="error" formaction="?/logout">
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
</style>
