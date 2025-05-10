<script lang="ts">
  import type { Spell } from "$lib/util/spell";
  import SpellCard from "../SpellCard.svelte";

  interface Props {
    char_id: number;
    spells: Spell[];
    feat_name: string;
    feat_desc: string;
    lvl_1_spell_slots: number;
    lvl_2_spell_slots: number;
    lvl_3_spell_slots: number;
    lvl_4_spell_slots: number;
    rages: number;
    rage_damage: number;
    second_wind: number;
    martial_arts: string;
    sneak_attack: string;
  }

  let props: Props = $props();
  let showMore = $state(true);

  function toggleShowMore(): void {
    showMore = !showMore;
  }

  function updateLvl1Slots(): void {
    const lvl1SlotInput = document.getElementById("lvl-1-slot-input") as HTMLInputElement;
    const lvl1Slots = lvl1SlotInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-lvl1-spell-slots", lvl1Slots.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getLvl1Slots(): number {
    const lvl1Slots = localStorage.getItem(props.char_id + "-lvl1-spell-slots");
    if (!lvl1Slots) {
      return props.lvl_1_spell_slots;
    }
    return Number(lvl1Slots);
  }

  function updateLvl2Slots(): void {
    const lvl2SlotInput = document.getElementById("lvl-2-slot-input") as HTMLInputElement;
    const lvl2Slots = lvl2SlotInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-lvl2-spell-slots", lvl2Slots.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getLvl2Slots(): number {
    const lvl2Slots = localStorage.getItem(props.char_id + "-lvl2-spell-slots");
    if (!lvl2Slots) {
      return props.lvl_2_spell_slots;
    }
    return Number(lvl2Slots);
  }

  function updateLvl3Slots(): void {
    const lvl3SlotInput = document.getElementById("lvl-3-slot-input") as HTMLInputElement;
    const lvl3Slots = lvl3SlotInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-lvl3-spell-slots", lvl3Slots.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getLvl3Slots(): number {
    const lvl3Slots = localStorage.getItem(props.char_id + "-lvl3-spell-slots");
    if (!lvl3Slots) {
      return props.lvl_3_spell_slots;
    }
    return Number(lvl3Slots);
  }

  function updateLvl4Slots(): void {
    const lvl4SlotInput = document.getElementById("lvl-4-slot-input") as HTMLInputElement;
    const lvl4Slots = lvl4SlotInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-lvl4-spell-slots", lvl4Slots.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getLvl4Slots(): number {
    const lvl4Slots = localStorage.getItem(props.char_id + "-lvl4-spell-slots");
    if (!lvl4Slots) {
      return props.lvl_4_spell_slots;
    }
    return Number(lvl4Slots);
  }

  function updateRages(): void {
    const rageInput = document.getElementById("rage-input") as HTMLInputElement;
    const rages = rageInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-rages", rages.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getRages(): number {
    const rages = localStorage.getItem(props.char_id + "-rages");
    if (!rages) {
      return props.rages;
    }
    return Number(rages);
  }

  function updateSecondWind(): void {
    const secondWindInput = document.getElementById("second-wind-input") as HTMLInputElement;
    const secondWind = secondWindInput.valueAsNumber;
    try {
      localStorage.setItem(props.char_id + "-second-wind", secondWind.toString());
    } catch (e: any) {
      console.log("Local storage access failure. ", e);
    }
  }
  function getSecondWindUses(): number {
    const secondWind = localStorage.getItem(props.char_id + "-second-wind");
    if (!secondWind) {
      return props.second_wind;
    }
    return Number(secondWind);
  }
</script>

{#if props.feat_name !== "Spellcasting"}
  <div class="spells">
    <div class="feat-header">
      <strong>{props.feat_name}</strong>
      <div class="show-more">
        <button class="pseudo show-more" onclick="{() => {toggleShowMore()}}">
          {#if showMore}
            <img src="updown-icon.svg" alt="Less Feat Info Button">
          {:else}
            <img src="dropdown-icon.svg" alt="More Feat Info Button">
          {/if}
        </button>
      </div>
    </div>
    {#if showMore}
      <p class="feat-desc">
        {#each props.feat_desc as chr}
          {#if chr === "\n"}<br><br>{:else if chr === "-"}&#x2022;{:else}{chr}{/if}
        {/each}
      </p>
    {/if}
  </div>
{/if}

<div class="spells spell-list">
  {#if props.lvl_1_spell_slots > 0}
    <div class="feat-stat">
      <strong>Level 1 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getLvl1Slots()} id="lvl-1-slot-input"
          onchange="{() => {updateLvl1Slots()}}">
        <span>/ {props.lvl_1_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_2_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 2 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getLvl2Slots()} id="lvl-2-slot-input"
          onchange="{() => {updateLvl2Slots()}}">
        <span>/ {props.lvl_2_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_3_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 3 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getLvl3Slots()} id="lvl-3-slot-input"
          onchange="{() => {updateLvl3Slots()}}">
        <span>/ {props.lvl_3_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_4_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 4 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getLvl4Slots()} id="lvl-4-slot-input"
          onchange="{() => {updateLvl4Slots()}}">
        <span>/ {props.lvl_4_spell_slots}</span>
      </div>
    </div>
  {/if}

  {#if props.rages > 0}
    <div class="feat-stat">
      <strong>Rage Uses:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getRages()} id="rage-input"
          onchange="{() => {updateRages()}}">
        <span>/ {props.rages}</span>
      </div>
    </div>
  {/if}
  {#if props.rage_damage > 0}
    <div class="feat-stat middle no-input">
      <strong>Rage Damage:</strong>
      <div>
        <span>+{props.rage_damage}</span>
      </div>
    </div>
  {/if}

  {#if props.second_wind > 0}
    <div class="feat-stat">
      <strong>Second Wind Uses:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={getSecondWindUses()} id="second-wind-input"
          onchange="{() => {updateSecondWind()}}">
        <span>/ {props.second_wind}</span>
      </div>
    </div>
  {/if}

  {#if props.martial_arts}
    <div class="feat-stat no-input">
      <strong>Martial Arts Die:</strong>
      <div>
        <span>{props.martial_arts}</span>
      </div>
    </div>
  {/if}

  {#if props.sneak_attack}
    <div class="feat-stat no-input">
      <strong>Sneak Attack Dice:</strong>
      <div>
        <span>{props.sneak_attack}</span>
      </div>
    </div>
  {/if}
</div>

{#if props.spells.length > 0}
  <div class="spells spell-list">
    <strong>Spells</strong>
    <div class="spell-cards">
      {#each props.spells as spell}
        <SpellCard spell={spell} />
      {/each}
    </div>
  </div>
{/if}

<style>
  div.spells {
    width: 19em;
    margin: auto;
    margin-top: 1em;
    border-style: solid;
    border-color: rgb(118, 155, 255);
    border-width: 0.2em;
    border-radius: 0.5em;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  div.spell-cards {
    margin-top: 0.5em;
    font-size: 0.75em;
  }

  p.feat-desc {
    font-size: 0.75em;
  }

  div.show-more {
    display: flex;
    justify-content: end;
    flex-grow: 1;
  }

  button.show-more {
    display: flex;
    padding: 0;
    padding: 0.25em;
  }

  div.feat-header {
    display: flex;
    align-items: center;
  }

  div.feat-header strong {
    display: flex;
    align-items: center;
  }

  .xp-input {
    width: 4.5em;
    margin-right: 0.25em;
  }

  div.feat-stat {
    background-color: rgb(196, 230, 242);
    border-radius: 0.5em;
    padding: 0.5em;
    padding-top: 0.25em;
    padding-bottom: 0.25em;
    display: flex;
    align-items: center;
  }

  div.feat-stat div {
    flex-grow: 1;
    display: flex;
    justify-content: end;
    align-items: center;
  }

  .middle {
    margin-top: 0.5em;
  }

  .no-input {
    height: 2.5em;
  }

  div.spell-list {
    margin-bottom: 1em;
  }
</style>
