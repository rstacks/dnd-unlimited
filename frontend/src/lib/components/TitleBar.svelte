<script lang="ts">
  let { account_modal_class }: { account_modal_class: string } = $props();
</script>

<header class="flex five">
  <div class="logo off-fifth three-fifth">
    <img src="favicon.svg" alt="DnD Unlimited Logo">
    <h1>DnD Unlimited</h1>
  </div>
  <div class="view-account">
    <label for="{account_modal_class}" class="button pseudo">
      <img src="account-icon-black.svg" alt="View Account Button">
    </label>
  </div>
</header>

<style>
  header {
    position: fixed;
    background-color: white;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-left: none;
    border-right: none;
    border-top: none;
    z-index: 3;
  }

  .view-account {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: end;
    align-items: center;
  }

  .view-account label {
    margin: 0;
    margin-right: 0.5em;
    padding: 0.4em;
    height: fit-content;
  }

  .view-account label img {
    width: 1.5em;
    padding-top: 0.35em;
  }

  .logo {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.6em;
    padding: 0.5em;
  }

  .logo img {
    width: 4em;
    margin-right: 1em;
  }
</style>