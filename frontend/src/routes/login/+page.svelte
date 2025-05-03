<svelte:head>
  <title>Login | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
</script>

<Title />

<article class="card">
  <h2>Log In</h2>
  <form method="POST" action="?/login">
    <label><input type="tel" inputmode="numeric" name="phone" placeholder="Phone Number" class="phone-input"></label>
    <input type="submit" class="register" value="Log In">
    <input formaction="?/register" class="pseudo register" type="submit" value="No account yet? Register">
  </form>
</article>

<style>
  article {
    max-width: 25em;
    width: 75%;
    justify-content: center;
    margin: auto;
    text-align: center;
  }

  .register {
    display: block;
    margin: auto;
    margin-bottom: 0.5em;
  }

  .phone-input {
    width: 75%;
    margin-bottom: 1em;
  }
</style>
