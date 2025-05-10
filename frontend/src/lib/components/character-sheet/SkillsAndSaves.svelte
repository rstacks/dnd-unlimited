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

<div>
  <strong>Saving Throws</strong>
  <ul>
    <li>
      {#if props.charSaves.includes("Strength")}
        <strong>Strength:</strong>
        <strong>{getProficientModText(props.str, props.proficiency_bonus)}</strong>
      {:else}
        <span>Strength:</span>
        <span>{getAbilityModText(props.str)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Dexterity")}
        <strong>Dexterity:</strong>
        <strong>{getProficientModText(props.dex, props.proficiency_bonus)}</strong>
      {:else}
        <span>Dexterity:</span>
        <span>{getAbilityModText(props.dex)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Constitution")}
        <strong>Constitution:</strong>
        <strong>{getProficientModText(props.con, props.proficiency_bonus)}</strong>
      {:else}
        <span>Constitution:</span>
        <span>{getAbilityModText(props.con)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Intelligence")}
        <strong>Intelligence:</strong>
        <strong>{getProficientModText(props.intl, props.proficiency_bonus)}</strong>
      {:else}
        <span>Intelligence:</span>
        <span>{getAbilityModText(props.intl)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Wisdom")}
        <strong>Wisdom:</strong>
        <strong>{getProficientModText(props.wis, props.proficiency_bonus)}</strong>
      {:else}
        <span>Wisdom:</span>
        <span>{getAbilityModText(props.wis)}</span>
      {/if}
    </li>
    <li>
      {#if props.charSaves.includes("Charisma")}
        <strong>Charisma:</strong>
        <strong>{getProficientModText(props.cha, props.proficiency_bonus)}</strong>
      {:else}
        <span>Charisma:</span>
        <span>{getAbilityModText(props.cha)}</span>
      {/if}
    </li>
  </ul>
</div>

<div>
  <strong>Skills</strong>
  <ul>
    {#each props.skills as skill}
      <li>
        {#if props.charSkills.includes(skill.skill_name)}
          <strong>{skill.skill_name}:</strong>
          <strong>{getSkillModText(skill.ability_name, true)}</strong>
        {:else}
          <span>{skill.skill_name}:</span>
          <span>{getSkillModText(skill.ability_name, false)}</span>
        {/if}
      </li>
    {/each}
  </ul>
</div>
