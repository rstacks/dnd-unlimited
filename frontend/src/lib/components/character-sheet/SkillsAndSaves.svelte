<script lang="ts">
  import type { Skill } from "$lib/util/character";
  import { getAbilityModText, getAbilityModifier } from "$lib/util/character-functions";

  interface Props {
    skills: Skill[];
    str: number;
    dex: number;
    con: number;
    intl: number;
    wis: number;
    cha: number;
    proficiency_bonus: number;
    charSaves: string[];
    charSkills: string[];
  }

  let props: Props = $props();

  function getProficientModText(abilityScore: number, profBonus: number): string {
    const rawAbilityMod = getAbilityModifier(abilityScore);
    const proficientMod = rawAbilityMod + profBonus;
    if (proficientMod >= 0) {
      return "+" + proficientMod.toFixed(0);
    }
    return proficientMod.toFixed(0);
  }

  function getSkillModText(skillAbilityName: string, proficient: boolean): string {
    if (skillAbilityName === "str") {
      if (proficient) {
        return getProficientModText(props.str, props.proficiency_bonus);
      }
      return getAbilityModText(props.str);
    }
    if (skillAbilityName === "dex") {
      if (proficient) {
        return getProficientModText(props.dex, props.proficiency_bonus);
      }
      return getAbilityModText(props.dex);
    }
    if (skillAbilityName === "con") {
      if (proficient) {
        return getProficientModText(props.con, props.proficiency_bonus);
      }
      return getAbilityModText(props.con);
    }
    if (skillAbilityName === "intl") {
      if (proficient) {
        return getProficientModText(props.intl, props.proficiency_bonus);
      }
      return getAbilityModText(props.intl);
    }
    if (skillAbilityName === "wis") {
      if (proficient) {
        return getProficientModText(props.wis, props.proficiency_bonus);
      }
      return getAbilityModText(props.wis);
    }

    // skillAbilityName === "cha"
    if (proficient) {
      return getProficientModText(props.cha, props.proficiency_bonus);
    }
    return getAbilityModText(props.cha);
  }
</script>

<div class="saves">
  <strong>Saving Throws</strong>
  <ul>
    <li>
      {#if props.charSaves.includes("Strength")}
        <strong class="label-text">Strength:</strong>
        <strong class="value-text">{getProficientModText(props.str, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Strength:</span>
        <span class="value-text">{getAbilityModText(props.str)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Dexterity")}
        <strong class="label-text">Dexterity:</strong>
        <strong class="value-text">{getProficientModText(props.dex, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Dexterity:</span>
        <span class="value-text">{getAbilityModText(props.dex)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Constitution")}
        <strong class="label-text">Constitution:</strong>
        <strong class="value-text">{getProficientModText(props.con, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Constitution:</span>
        <span class="value-text">{getAbilityModText(props.con)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Intelligence")}
        <strong class="label-text">Intelligence:</strong>
        <strong class="value-text">{getProficientModText(props.intl, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Intelligence:</span>
        <span class="value-text">{getAbilityModText(props.intl)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Wisdom")}
        <strong class="label-text">Wisdom:</strong>
        <strong class="value-text">{getProficientModText(props.wis, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Wisdom:</span>
        <span class="value-text">{getAbilityModText(props.wis)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Charisma")}
        <strong class="label-text">Charisma:</strong>
        <strong class="value-text">{getProficientModText(props.cha, props.proficiency_bonus)}</strong>
      {:else}
        <span class="label-text">Charisma:</span>
        <span class="value-text">{getAbilityModText(props.cha)}</span>
      {/if}
    </li>
  </ul>
</div>

<div class="skills">
  <strong>Skills</strong>
  <ul>
    {#each props.skills as skill}
      <li>
        {#if props.charSkills.includes(skill.skill_name)}
          <strong class="label-text">{skill.skill_name}:</strong>
          <strong class="value-text">{getSkillModText(skill.ability_name, true)}</strong>
        {:else}
          <span class="label-text">{skill.skill_name}:</span>
          <span class="value-text">{getSkillModText(skill.ability_name, false)}</span>
        {/if}
      </li>
    {/each}
  </ul>
</div>

<style>
  div.saves {
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    width: 19em;
    margin: auto;
    margin-top: 1em;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  div.skills {
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    width: 19em;
    margin: auto;
    margin-top: 1em;
    margin-bottom: 1em;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  ul {
    list-style-type: none;
    padding-left: 0;
    width: 15em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  li {
    display: flex;
    background-color: rgb(196, 230, 242);
    border-radius: 0.5em;
    margin-top: 0.25em;
    padding: 0.5em;
    width: 12em;
  }

  .label-text {
    width: 9em;
  }

  .value-text {
    text-align: center;
    flex-grow: 1;
  }
</style>
