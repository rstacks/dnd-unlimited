<svelte:head>
  <title>Login | DnD Unlimited</title>
</svelte:head>

<script lang="ts">

</script>

<article>
  <form method="POST" action="?/login">
    <label><input type="number" placeholder="Phone Number"></label>
    <input type="submit" value="Log In">
    <input formaction="?/register" class="pseudo" type="submit" value="No account yet? Register">
  </form>
</article>
