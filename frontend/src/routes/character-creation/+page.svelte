<svelte:head>
  <title>Character Creation | DnD Unlimited</title>
</svelte:head>
  
<script lang="ts">
  import ClassCard from "$lib/components/ClassCard.svelte";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();

  function deselectOtherClasses(buttonToSelectId: string): void {
    const otherButtons = <HTMLCollectionOf<HTMLInputElement>>document.getElementsByClassName("class-button");
    for (const button of otherButtons) {
      button.checked = false;
    }
    const buttonToSelect = document.getElementById(buttonToSelectId) as HTMLInputElement;
    buttonToSelect.checked = true;
  }
</script>

<article class="card char-creation-screen" id="char-creation-screen">
  <header class="char-creation-header">
    <label for="leave-modal" class="back-button pseudo button">
      <img src="back-icon.svg" alt="Back to Dashboard Button">
    </label>
    <h3>Character Creation</h3>
  </header>
  <div class="spacer"></div>
  <div class="tabs three char-creation-form">
    <input id="tab-1" type="radio" name="char-creation-tabs" checked />
    <label for="tab-1" class="button pseudo toggle">Basic Info</label>
    /
    <input id="tab-2" type="radio" name="char-creation-tabs" />
    <label for="tab-2" class="button pseudo toggle">Class</label>
    /
    <input id="tab-3" type="radio" name="char-creation-tabs" />
    <label for="tab-3" class="button pseudo toggle">Ability Scores</label>
    <div class="row form-tabs">
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

        <div class="basic-info-field">
          <label for="bkg-info">Background Info:</label>
          <textarea name="bkg-info" id="bkg-info-input"
            placeholder="Background Info (Optional)"></textarea>
        </div>
      </div>

      <div>
        {#each data.classes as classData}
          <div class="class-selector">
            <label>
              <input class="class-button" checked={false} name="button-{classData.id}"
                type="radio" oninput="{() => { deselectOtherClasses("button-" + classData.id) }}"
                id="button-{classData.id}">
              <span class="checkable"></span>
            </label>
            <ClassCard classData={classData} allClasses={data.classes} />
          </div>
        {/each}
      </div>

      <div class="ability-scores">
        <label for="ability-score-info" class="ability-score-info-button pseudo button">
          How do I assign ability scores?
        </label>
        <div class="flex two input-grid">
          <div class="score-label">
            <label for="str">Strength:</label>
          </div>
          <div class="score-input">
            <input name="str" type="number" placeholder="STR" />
          </div>
  
          <div class="score-label">
            <label for="dex">Dexterity:</label>
          </div>
          <div class="score-input">
            <input name="dex" type="number" placeholder="DEX" />
          </div>
  
          <div class="score-label">
            <label for="con">Constitution:</label>
          </div>
          <div class="score-input">
            <input name="con" type="number" placeholder="CON" />
          </div>
  
          <div class="score-label">
            <label for="int">Intelligence:</label>
          </div>
          <div class="score-input">
            <input name="int" type="number" placeholder="INT" />
          </div>
  
          <div class="score-label">
            <label for="wis">Wisdom:</label>
          </div>
          <div class="score-input">
            <input name="wis" type="number" placeholder="WIS" />
          </div>
  
          <div class="score-label">
            <label for="cha">Charisma:</label>
          </div>
          <div class="score-input">
            <input name="cha" type="number" placeholder="CHA" />
          </div>
        </div>
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
    <footer class="leave-modal-foot">
      <a class="button dangerous exit-button" href="/dashboard">Leave Character Creation</a>
    </footer>
  </article>
</div>

<div class="modal">
  <input type="checkbox" id="ability-score-info">
  <label for="ability-score-info" class="overlay"></label>
  <article>
    <header>
      <h3>Assigning Ability Scores</h3>
      <label for="ability-score-info" class="close">&times;</label>
    </header>
    <section class="content">
      Follow the steps below to assign
      your ability scores. Your DM can also help you with this!
      <ol>
        <li>Roll four d6.</li>
        <li>Drop the lowest roll.</li>
        <li>Record the sum of the remaining three dice.</li>
        <li>Repeat steps 1 through 3 until you have six sums.</li>
        <li>Assign each sum to one of your ability scores.</li>
      </ol>
    </section>
  </article>
</div>

<style>
  .char-creation-screen {
    height: 100%;
    width: 100%;
    border-style: none;
    border-radius: 0;
    overflow: auto;
  }

  .char-creation-header {
    position: fixed;
    display: flex;
    align-items: center;
    width: 100%;
    z-index: 1;
    background-color: white;
  }

  .spacer {
    margin-top: 4em;
  }

  .back-button {
    display: flex;
    padding: 0.25em;
    margin-right: 1em;
  }

  .leave-modal-foot {
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

  .form-tabs label {
    cursor: default;
  }

  .basic-info input {
    width: 15em;
  }

  .basic-info-field {
    margin-top: 1em;
  }

  .basic-info-field label {
    display: block;
  }

  textarea {
    width: 15em;
    height: 10em;
    resize: vertical;
  }

  .ability-scores input {
    width: 7.5em;
  }

  .score-label {
    display: flex;
    justify-content: end;
    align-items: center;
    margin-top: 1em;
    padding-right: 1em;
  }

  .score-input {
    text-align: left;
    margin-top: 1em;
    padding-left: 0;
  }

  .class-selector {
    display: flex;
    align-items: center;
    width: fit-content;
    margin: auto;
  }

  .ability-score-info-button {
    color: rgb(124, 124, 124);
    text-decoration: dotted;
    text-decoration-line: underline;
  }

  .ability-score-info-button:hover {
    cursor: pointer;
  }
</style>
