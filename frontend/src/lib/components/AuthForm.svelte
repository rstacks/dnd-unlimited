<script lang="ts">
  interface Props {
    formtypeProp?: "login" | "register";
    loginAction?: string;
    registerAction?: string;
  }

  let {
    formtypeProp = "login",
    loginAction = "?/login",
    registerAction = "?/register"
  }: Props = $props();
  
  let formtype: "login" | "register" = $state(formtypeProp);

  function switchFormtype(currentFormtype: "login" | "register"): void {
    if (currentFormtype === "login") {
      formtype = "register";
    } else if (currentFormtype === "register") {
      formtype = "login";
    }
  }
</script>

<article class="card">
  {#if formtype === "login"}
    <h2>Log In</h2> 
  {:else if formtype === "register"}
    <h2>Register</h2>
  {/if}
  
  <form method="POST" action={loginAction}>
    <label>
      <input type="tel" inputmode="numeric" name="phone" placeholder="Phone Number"
        class="phone-input" autocomplete="off">
    </label>

    {#if formtype === "register"}
      <label>
        <input type="text" name="user-name" placeholder="Name"
          class="phone-input" autocomplete="off">
      </label>
    {/if}
    
    {#if formtype === "login"}
      <input type="submit" class="login" value="Log In">
    {:else if formtype === "register"}
      <input type="submit" class="login" value="Register" formaction={registerAction}>
    {/if}
  </form>
  
  <button class="pseudo register" onclick="{() => { switchFormtype(formtype) }}">
    {#if formtype === "login"}
      No account yet? Register
    {:else if formtype === "register"}
      Returning user? Login
    {/if}
  </button>
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