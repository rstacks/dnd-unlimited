<svelte:head>
  <title>Login | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
</script>

<Title />

<article class="card">
  <h2>Log In</h2>
  <form method="POST">
    <label>
      <input type="tel" inputmode="numeric" name="phone" placeholder="Phone Number"
        class="phone-input" autocomplete="off">
    </label>
    <input type="submit" class="login" value="Log In">
  </form>
  <a class="pseudo button register" href="/">No account yet? Register</a>
</article>

<style>
  article {
    max-width: 25em;
    width: 75%;
    justify-content: center;
    margin: auto;
    text-align: center;
  }

  .login {
    display: block;
    margin: auto;
    margin-bottom: 0.5em;
  }

  .register {
    width: fit-content;
    margin: auto;
    margin-bottom: 0.5em;
  }

  .phone-input {
    width: 75%;
    margin-bottom: 1em;
  }
</style>
