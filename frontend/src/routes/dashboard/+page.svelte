<svelte:head>
  <title>Dashboard | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import TitleBar from "$lib/components/TitleBar.svelte";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();
</script>

<TitleBar account_modal_class="my-modal" />

<h2>Welcome, {data.name}!</h2>

<div class="modal">
  <input type="checkbox" id="my-modal">
  <label for="my-modal" class="overlay"></label>
  <article>
    <header>
      <h3>Account</h3>
      <label for="my-modal" class="close">&times;</label>
    </header>
    <form method="POST" action="?/logout">
      <section class="content">
        <label for="user-name" class="name-label">Name:</label>
        <input type="text" name="user-name" placeholder="Name"
          autocomplete="off" value="{data.name}" class="name-input">
      </section>
      <footer class="flex">
        <div class="logout-button">
          <input type="submit" value="Log Out" class="error">
        </div>
        <div class="save-button">
          <input type="submit" value="Save">
        </div>
      </footer>
    </form>
  </article>
</div>

<style>
  h2 {
    padding-top: 3em;
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

  .logout-button {
    margin-left: 1em;
    padding: 0;
  }

  .save-button {
    display: flex;
    justify-content: end;
    margin-right: 0.5em;
    padding: 0;
  }
</style>
