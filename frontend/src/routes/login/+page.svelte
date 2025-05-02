<svelte:head>
  <title>Login | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
  // TODO: make it so you can only enter numbers into phone number form
</script>

<Title />

<article class="card boxed centered">
  <h2>Log In</h2>
  <form method="POST" action="?/login">
    <label><input type="text" name="phone" placeholder="Phone Number" class="phone-input"></label>
    <input type="submit" class="register" value="Log In">
    <input formaction="?/register" class="pseudo register" type="submit" value="No account yet? Register">
  </form>
</article>

<style>
  .boxed {
    max-width: 25em;
    width: 75%;
  }

  .centered {
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
