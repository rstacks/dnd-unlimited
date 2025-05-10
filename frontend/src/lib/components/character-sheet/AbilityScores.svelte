<script lang="ts">
  import { getAbilityModText } from "$lib/util/character-functions";

  interface Props {
    str: number;
    dex: number;
    con: number;
    intl: number;
    wis: number;
    cha: number;
  }

  let props: Props = $props();
</script>

<div class="ability-scores">
  <div class="score-container">
    <strong>Strength</strong>
    <span class="score">{props.str}</span>
    <div>
      <span>{getAbilityModText(props.str)}</span>
    </div>
  </div>
  <div class="score-container">
    <strong>Dexterity</strong>
    <span class="score">{props.dex}</span>
    <div>
      <span>{getAbilityModText(props.dex)}</span>
    </div>
  </div>
  <div class="score-container">
    <strong>Constitution</strong>
    <span class="score">{props.con}</span>
    <div>
      <span>{getAbilityModText(props.con)}</span>
    </div>
  </div>
  <div class="score-container">
    <strong>Intelligence</strong>
    <span class="score">{props.intl}</span>
    <div>
      <span>{getAbilityModText(props.intl)}</span>
    </div>
  </div>
  <div class="score-container">
    <strong>Wisdom</strong>
    <span class="score">{props.wis}</span>
    <div>
      <span>{getAbilityModText(props.wis)}</span>
    </div>
  </div>
  <div class="score-container">
    <strong>Charisma</strong>
    <span class="score">{props.cha}</span>
    <div>
      <span>{getAbilityModText(props.cha)}</span>
    </div>
  </div>
</div>

<style>
  div.ability-scores {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    width: 19em;
    margin: auto;
    margin-top: 1em;
    margin-bottom: 1em;
  }

  div.score-container {
    display: flex;
    flex-direction: column;
    background-color: rgb(196, 230, 242);
    border-radius: 0.5em;
    width: 7em;
    padding: 0.5em;
    align-items: center;
    margin: auto;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  div.score-container div {
    background-color: rgb(169, 191, 253);
    padding: 0.25em;
    padding-left: 0.5em;
    padding-right: 0.5em;
    border-radius: 0.5em;
    width: 3em;
    text-align: center;
  }

  span.score {
    margin-top: 0.25em;
    margin-bottom: 0.25em;
  }
</style>
