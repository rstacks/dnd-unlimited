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
  <div class="tabs three char-creation-form">
    <input id="tab-1" type="radio" name="char-creation-tabs" checked />
    <label for="tab-1" class="button pseudo toggle">Basic Info</label>
    /
    <input id="tab-2" type="radio" name="char-creation-tabs" />
    <label for="tab-2" class="button pseudo toggle">Class</label>
    /
    <input id="tab-3" type="radio" name="char-creation-tabs" />
    <label for="tab-3" class="button pseudo toggle">Ability Scores</label>
    <div class="row">
      <div class="basic-info">
        <div class="basic-info-field">
          <label for="char-name">Character Name:</label>
          <input name="char-name" type="text" placeholder="Character Name" />
        </div>
        
        <div class="basic-info-field">
          <label for="melee-wep">Melee Weapon:</label>
          <input name="melee-wep" type="text" placeholder="Melee Weapon Name" />
        </div>
        
        <div class="basic-info-field">
          <label for="ranged-wep">Ranged Weapon:</label>
          <input name="ranged-wep" type="text" placeholder="Ranged Weapon Name" />
        </div>
      </div>

      <div>
        zone 2
      </div>

      <div>
        zone 3
      </div>
    </div>
  </div>
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

  .char-creation-form {
    text-align: center;
    margin: auto;
  }

  .basic-info input {
    width: 15em;
  }

  .basic-info-field {
    margin-top: 1em;
  }

  .basic-info-field label {
    display: block;
    cursor: default;
  }
</style>
  
  