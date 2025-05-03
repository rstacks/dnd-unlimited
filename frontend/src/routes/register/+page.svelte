<svelte:head>
  <title>Register | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
</script>

<Title />

<article class="card">
  <h2>Register</h2>
  <form method="POST">
    <label>
      <input type="tel" inputmode="numeric" name="phone" placeholder="Phone Number"
        class="phone-input" autocomplete="off">
    </label>
    <label>
      <input type="text" name="name" placeholder="Name"
        class="phone-input" autocomplete="off">
    </label>
    <input type="submit" class="login" value="Register">
  </form>
  <a class="pseudo button register" href="/login">Returning user? Login</a>
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
