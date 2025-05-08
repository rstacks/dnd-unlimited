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
      <img class="class-icon" src="{"class-icons/" + character.class_name.toLowerCase() + ".svg"}"
        alt="{character.class_name + " class icon"}">
      <div class="content">
        <h3>{character.character_name}</h3>
        <p>Level {character.lvl} {character.class_name}</p>
        <span>{character.xp}/{xpGoal} XP</span>
      </div>
      <div class="close-button">
        <button onclick="{() => {show = false}}">
          &times;
        </button>
      </div>
    </header>
  </article>
</div>

<style>
  .character-sheet {
    position: absolute;
    z-index: 5;
    top: 7.75em;
    left: 0.2em;
    right: 0.2em;
  }

  article {
    max-width: 60em;
    margin: auto;
  }

  header {
    display: flex;
    align-items: center;
  }

  header img {
    width: 5em;
  }
</style>
