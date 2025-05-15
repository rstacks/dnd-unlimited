<svelte:head>
  <title>Login | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
  import Loading from "$lib/components/Loading.svelte";
  import { beforeNavigate } from "$app/navigation";
  import { onMount } from "svelte";
  import { isIosBrowser } from "$lib/util/util";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();
  
  let formtype: "login" | "register" = $state("login");
  formtype = (data.onRegisterForm && data.onRegisterForm === "true") ? "register" : "login";
  function switchFormtype(currentFormtype: "login" | "register"): void {
    if (currentFormtype === "login") {
      formtype = "register";
    } else if (currentFormtype === "register") {
      formtype = "login";
    }
  }

  let badPhone = $state(false); 
  if (data.badPhone && data.badPhone === "true") {
    badPhone = true;
  }
  let badName = $state(false);
  if (data.badName && data.badName === "true") {
    badName = true;
  }
  let accountNotFound = $state(false);
  if (data.accountNotFound && data.accountNotFound === "true") {
    accountNotFound = true;
  }
  let accountAlreadyExists = $state(false);
  if (data.accountAlreadyExists && data.accountAlreadyExists === "true") {
    accountAlreadyExists = true;
  }

  let showInvalidPhoneStyle = $state(true);
  let showInvalidNameStyle = $state(true);
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

<Title />

<article class="card">
  {#if formtype === "login"}
    <h2>Log In</h2> 
  {:else if formtype === "register"}
    <h2>Register</h2>
  {/if}
  
  <form method="POST" action="?/login">
    <label>
      <input type="tel" inputmode="numeric" name="phone" placeholder="Phone Number"
        class="phone-input" autocomplete="off"
        style:margin-bottom="{((badPhone || accountNotFound || accountAlreadyExists) && showInvalidPhoneStyle) ? "0em" : "1em"}"
        style:background-color="{(badPhone && showInvalidPhoneStyle) ? "rgb(253, 183, 183)" : "white"}"
        oninput="{() => showInvalidPhoneStyle = false}">
    </label>
    {#if badPhone && showInvalidPhoneStyle}
      <span>Please enter a valid phone number.</span>
    {:else if accountNotFound && showInvalidPhoneStyle}
      <span>Account not found. Have you registered?</span>
    {:else if accountAlreadyExists && showInvalidPhoneStyle}
      <span>Phone number already in use. Log in instead?</span>
    {/if}

    {#if formtype === "register"}
      <label>
        <input type="text" name="user-name" placeholder="Name"
          class="phone-input" autocomplete="off"
          style:margin-bottom="{(badName && showInvalidNameStyle) ? "0em" : "1em"}"
          style:background-color="{(badName && showInvalidNameStyle) ? "rgb(253, 183, 183)" : "white"}"
          oninput="{() => showInvalidNameStyle = false}">
      </label>
      {#if badName && showInvalidNameStyle}
        <span>Please enter your name.</span>
      {/if}
    {/if}
    
    {#if formtype === "login"}
      <input type="submit" class="login" value="Log In"
        onclick="{() => { showLoading = true }}">
    {:else if formtype === "register"}
      <input type="submit" class="login" value="Register" formaction="?/register"
        onclick="{() => { showLoading = true }}">
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

  span {
    color: red;
    display: block;
    font-size: 0.75em;
    margin-bottom: 1em;
  }
</style>
