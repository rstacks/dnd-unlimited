<svelte:head>
  <title>Character Creation | DnD Unlimited</title>
</svelte:head>
  
<script lang="ts">
  import ClassCard from "$lib/components/ClassCard.svelte";
  import CharacterSummary from "$lib/components/CharacterSummary.svelte";
  import type { PageProps } from "./$types";
  import type { ClassData } from "$lib/util/class";
  import type { AbilityScores } from "$lib/util/character";

  interface BasicInfoInputs {
    name: string;
    meleeWep: string;
    rangedWep: string;
    notes: string;
  }

  interface CharacterFormInputs {
    basicInfo: BasicInfoInputs;
    classData: ClassData | undefined;
    abilityScores: AbilityScores;
  }

  let { data }: PageProps = $props();
  let classSelectedStatuses = $state(data.classSelectedList);
  let characterFormInputs: CharacterFormInputs = $state({
    basicInfo: { name: "", meleeWep: "", rangedWep: "", notes: "" },
    classData: undefined,
    abilityScores: { str: 0, dex: 0, con: 0, intl: 0, wis: 0, cha: 0 }
  });

  function deselectOtherClasses(): void {
    const otherButtons = <HTMLCollectionOf<HTMLInputElement>>document.getElementsByClassName("class-button");
    for (const button of otherButtons) {
      button.checked = false;
    }
    for (const classSelectedStatus of classSelectedStatuses) {
      classSelectedStatus.selected = false;
    }
  }

  function selectClass(classId: number): void {
    const buttonToSelect = document.getElementById("button-" + classId) as HTMLInputElement;
    buttonToSelect.checked = true;
    classSelectedStatuses.find((elem) => classId === elem.classId)!.selected = true;
  }

  function isClassSelected(classId: number): boolean {
    const classSelectedStatus = classSelectedStatuses.find((elem) => classId === elem.classId);
    if (classSelectedStatus) {
      return classSelectedStatus.selected;
    }
    return false;
  }

  function getBasicInfoInputs(): BasicInfoInputs {
    const charInputElem = document.getElementById("char-name-input") as HTMLInputElement;
    const meleeInputElem = document.getElementById("melee-wep-input") as HTMLInputElement;
    const rangedInputElem = document.getElementById("ranged-wep-input") as HTMLInputElement;
    const backgroundInputElem = document.getElementById("bkg-info-input") as HTMLInputElement;

    return {
      name: charInputElem.value.trim(),
      meleeWep: meleeInputElem.value.trim(),
      rangedWep: rangedInputElem.value.trim(),
      notes: backgroundInputElem.value.trim()
    };
  }

  function getSelectedClass(): ClassData | undefined {
    const classId = classSelectedStatuses.find((elem) => elem.selected)?.classId;
    const classData = data.classes.find((elem) => elem.id === classId);
    return classData;
  }

  function getAbilityScoresInputs(): AbilityScores {
    const strInput = document.getElementById("str-input") as HTMLInputElement;
    const dexInput = document.getElementById("dex-input") as HTMLInputElement;
    const conInput = document.getElementById("con-input") as HTMLInputElement;
    const intInput = document.getElementById("int-input") as HTMLInputElement;
    const wisInput = document.getElementById("wis-input") as HTMLInputElement;
    const chaInput = document.getElementById("cha-input") as HTMLInputElement;

    return {
      str: strInput.valueAsNumber,
      dex: dexInput.valueAsNumber,
      con: conInput.valueAsNumber,
      intl: intInput.valueAsNumber,
      wis: wisInput.valueAsNumber,
      cha: chaInput.valueAsNumber
    };
  }

  function getCharacterFormInputs(): CharacterFormInputs {
    const basicInfo = getBasicInfoInputs();
    const classData = getSelectedClass();
    const abilityScores = getAbilityScoresInputs();
    
    return {
      basicInfo: basicInfo,
      classData: classData,
      abilityScores: abilityScores
    };
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
  <div class="tabs four char-creation-form">
    <input id="tab-1" type="radio" name="char-creation-tabs" checked />
    <label for="tab-1" class="button pseudo toggle char-tab">Basic Info</label>
    <span class="tab-separator">/</span>
    <input id="tab-2" type="radio" name="char-creation-tabs" />
    <label for="tab-2" class="button pseudo toggle char-tab">Class</label>
    <span class="tab-separator">/</span>
    <input id="tab-3" type="radio" name="char-creation-tabs" />
    <label for="tab-3" class="button pseudo toggle char-tab">Ability Scores</label>
    <span class="tab-separator">/</span>
    <input id="tab-4" type="radio" name="char-creation-tabs" />
    <label for="tab-4" class="button pseudo toggle char-tab">Create!</label>
    <div class="row form-tabs">
      <div class="basic-info">
        <div class="flex tab-arrow-group">
          <div class="arrow-right">
            <label class="button pseudo tab-arrow" for="tab-2">
              <span>Next</span>
              <img src="forward-arrow.svg" alt="Right Arrow for Next Tab">
            </label>
          </div>
        </div>
        <div class="basic-info-field">
          <label for="char-name">Character Name:</label>
          <input id="char-name-input" name="char-name" type="text" placeholder="Character Name"
            onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
        </div>
        
        <div class="basic-info-field">
          <label for="melee-wep">Melee Weapon:</label>
          <input id="melee-wep-input" name="melee-wep" type="text" placeholder="Melee Weapon Name"
            onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
        </div>
        
        <div class="basic-info-field">
          <label for="ranged-wep">Ranged Weapon:</label>
          <input id="ranged-wep-input" name="ranged-wep" type="text" placeholder="Ranged Weapon Name"
            onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
        </div>

        <div class="basic-info-field">
          <label for="bkg-info">Background Info:</label>
          <textarea name="bkg-info" id="bkg-info-input"
            placeholder="Background Info (Optional)"
            onchange="{() => {characterFormInputs = getCharacterFormInputs()}}"></textarea>
        </div>
      </div>

      <div>
        <div class="flex tab-arrow-group">
          <div>
            <label class="button pseudo tab-arrow" for="tab-1">
              <img src="backward-arrow.svg" alt="Left Arrow for Previous Tab">
              <span>Previous</span>
            </label>
          </div>
          <div class="arrow-right">
            <label class="button pseudo tab-arrow" for="tab-3">
              <span>Next</span>
              <img src="forward-arrow.svg" alt="Right Arrow for Next Tab">
            </label>
          </div>
        </div>
        <div class="class-list">
        {#each data.classes as classData}
          <div class="class-selector">
            <label>
              <input class="class-button" checked={false} name="button-{classData.id}"
                id="button-{classData.id}" type="radio" oninput="{() => {
                    deselectOtherClasses();
                    selectClass(classData.id);
                    characterFormInputs = getCharacterFormInputs();
                  }}" tabindex="-1">
              <span class="checkable class-button-text"></span>
            </label>
            <ClassCard classData={classData} allClasses={data.classes}
              selected={isClassSelected(classData.id)} allSpells={data.spells} />
          </div>
        {/each}
        </div>
      </div>

      <div class="ability-scores">
        <div class="flex tab-arrow-group">
          <div>
            <label class="button pseudo tab-arrow" for="tab-2">
              <img src="backward-arrow.svg" alt="Left Arrow for Previous Tab">
              <span>Previous</span>
            </label>
          </div>
          <div class="arrow-right">
            <label class="button pseudo tab-arrow" for="tab-4">
              <span>Next</span>
              <img src="forward-arrow.svg" alt="Right Arrow for Next Tab">
            </label>
          </div>
        </div>
        <label for="ability-score-info" class="ability-score-info-button pseudo button">
          How do I assign ability scores?
        </label>
        <div class="flex two input-grid">
          <div class="score-label">
            <label for="str">Strength:</label>
          </div>
          <div class="score-input">
            <input id="str-input" name="str" type="number" placeholder="STR" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
  
          <div class="score-label">
            <label for="dex">Dexterity:</label>
          </div>
          <div class="score-input">
            <input id="dex-input" name="dex" type="number" placeholder="DEX" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
  
          <div class="score-label">
            <label for="con">Constitution:</label>
          </div>
          <div class="score-input">
            <input id="con-input" name="con" type="number" placeholder="CON" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
  
          <div class="score-label">
            <label for="int">Intelligence:</label>
          </div>
          <div class="score-input">
            <input id="int-input" name="int" type="number" placeholder="INT" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
  
          <div class="score-label">
            <label for="wis">Wisdom:</label>
          </div>
          <div class="score-input">
            <input id="wis-input" name="wis" type="number" placeholder="WIS" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
  
          <div class="score-label">
            <label for="cha">Charisma:</label>
          </div>
          <div class="score-input">
            <input id="cha-input" name="cha" type="number" placeholder="CHA" tabindex="-1"
              onchange="{() => {characterFormInputs = getCharacterFormInputs()}}" />
          </div>
        </div>
      </div>

      <div>
        <div class="flex tab-arrow-group">
          <div>
            <label class="button pseudo tab-arrow" for="tab-3">
              <img src="backward-arrow.svg" alt="Left Arrow for Previous Tab">
              <span>Previous</span>
            </label>
          </div>
        </div>
        <CharacterSummary name={characterFormInputs.basicInfo.name}
          notes={characterFormInputs.basicInfo.notes}
          meleeWep={characterFormInputs.basicInfo.meleeWep}
          rangedWep={characterFormInputs.basicInfo.rangedWep}
          className={characterFormInputs.classData?.class_name}
          classId={characterFormInputs.classData?.id}
          abilityScores={characterFormInputs.abilityScores} />
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
    margin-bottom: 1em;
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

  .class-list {
    display: grid;
    width: fit-content;
    grid-template-columns: auto auto auto;
    column-gap: 3em;
    margin: auto;
  }

  @media (max-width: 1200px) {
    .class-list {
      grid-template-columns: auto auto;
    }
  }

  @media (max-width: 800px) {
    .class-list {
      grid-template-columns: auto;
    }
  }

  .class-button-text {
    font-size: 2em;
    padding: 0;
    padding-right: 0.6em;
  }

  .char-tab {
    font-size: 0.7em;
  }

  .tab-separator {
    vertical-align: middle;
  }

  .tab-arrow {
    display: flex;
    align-items: center;
    width: fit-content;
    font-size: 0.7em;
    margin-bottom: 0;
  }

  .tab-arrow:hover {
    cursor: pointer;
  }

  .tab-arrow img {
    width: 1.5em;
  }

  .arrow-right {
    display: flex;
    justify-content: right;
    margin-right: 1.2em;
  }

  .tab-arrow-group {
    margin: auto;
    max-width: 30em;
  }
</style>
