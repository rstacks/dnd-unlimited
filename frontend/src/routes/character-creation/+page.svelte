<svelte:head>
  <title>Character Creation | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  // TODO: reset form inputs when close button pressed
  // function closeCharacterCreation(): void {
  //   const elem = document.getElementById("char-creation-screen");
  //   if (elem) {
  //     elem.style.display = "none";
  //   }
  // }
</script>
  
<article class="card char-creation-screen" id="char-creation-screen">
  <header class="char-creation-header">
    <label for="leave-modal" class="back-button pseudo button">
      <img src="back-icon.svg" alt="Back to Dashboard Button">
    </label>
    <h3>Character Creation</h3>
  </header>
  <p>test</p>
</article>

<div class="modal">
  <input type="checkbox" id="leave-modal">
  <label for="leave-modal" class="overlay"></label>
  <article>
    <header>
      <h3>Confirm Exit</h3>
      <label for="leave-modal" class="close">&times;</label>
    </header>
    <section class="content">
      Are you sure you want to leave?
      <strong>All of your progress will be lost!</strong>
    </section>
    <footer>
      <a class="button dangerous exit-button" href="/dashboard">Leave Character Creation</a>
    </footer>
  </article>
</div>

<style>
  .char-creation-screen {
    position: fixed;
    height: 100%;
    width: 100%;
    border-style: none;
    border-radius: 0;
  }

  .char-creation-header {
    display: flex;
    align-items: center;
  }

  .back-button {
    display: flex;
    padding: 0.25em;
    margin-right: 1em;
  }

  footer {
    width: fit-content;
    margin: auto;
  }

  .exit-button {
    margin: auto;
    margin-bottom: 1em;
  }
</style>
  
  