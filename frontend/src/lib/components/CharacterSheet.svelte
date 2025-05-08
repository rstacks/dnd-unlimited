<script lang="ts">
  import type { Character } from "$lib/util/character";

  interface Props {
    character: Character;
    xpGoal: number;
    show: boolean;
  }

  let { character, xpGoal, show=$bindable() }: Props = $props();
</script>

<div class="character-sheet">
  <article class="card">
    <header>
      <div class="close-button">
        <button class="pseudo" onclick="{() => {show = false}}">
          <img src="back-icon.svg" alt="Back to Characters View Button">
        </button>
      </div>
      <img class="class-icon" src="{"class-icons/" + character.class_name.toLowerCase() + ".svg"}"
        alt="{character.class_name + " class icon"}">
      <div class="content">
        <h3>{character.character_name}</h3>
        <p>Level {character.lvl} {character.class_name}</p>
        <span>{character.xp}/{xpGoal} XP</span>
      </div>
    </header>
    <div class="tabs five">
      <input id="tab-1" type="radio" name="char-sheet-tabs" checked />
      <input id="tab-2" type="radio" name="char-sheet-tabs" />
      <input id="tab-3" type="radio" name="char-sheet-tabs" />
      <input id="tab-4" type="radio" name="char-sheet-tabs" />
      <input id="tab-5" type="radio" name="char-sheet-tabs" />
      <div class="row">
        <div>
          fuck
        </div>

        <div>
          shit
        </div>

        <div>
          balls
        </div>

        <div>
          cock
        </div>

        <div>
          damn
        </div>
      </div>
      <footer class="character-sheet-tab-buttons">
        <label for="tab-1" class="leftmost-tab">Overview</label>
        <label for="tab-2">Weapons & Items</label>  
        <label for="tab-3">Skills & Saves</label>  
        <label for="tab-4">Spells</label>  
        <label for="tab-5" class="rightmost-tab">Stats</label>  
      </footer>
    </div>
  </article>
</div>

<style>
  .character-sheet {
    position: absolute;
    z-index: 5;
    top: 7.75em;
    left: 0.2em;
    right: 0.2em;
    /* height: 80%; */
  }

  article {
    max-width: 60em;
    margin: auto;
    /* height: 100%; */
  }

  header {
    display: flex;
    align-items: center;
  }

  .class-icon {
    width: 5em;
  }

  .close-button button {
    display: flex;
    padding: 0.1em;
  }

  .close-button button img {
    width: 1.5em;
  }

  .character-sheet-tab-buttons {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    border-style: solid;
    border-color: rgb(168, 168, 168);
    border-width: 0.1em;
    border-bottom: 0;
    border-left: 0;
    border-right: 0;
    font-size: 0.75em;
    padding: 0;
  }

  .character-sheet-tab-buttons label {
    text-align: center;
    border-style: solid;
    border-color: rgb(168, 168, 168);
    border-width: 0.1em;
    border-top: 0;
    border-bottom: 0;
    border-right: 0;
  }

  .leftmost-tab {
    border-left: 0;
  }

  .rightmost-tab {
    border-right: 0;
  }
</style>
