<script lang="ts">
  import type { Spell } from "$lib/util/spell";
  import SpellCard from "../SpellCard.svelte";

  interface Props {
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
          value={props.lvl_1_spell_slots}>
        <span>/ {props.lvl_1_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_2_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 2 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={props.lvl_2_spell_slots}>
        <span>/ {props.lvl_2_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_3_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 3 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={props.lvl_3_spell_slots}>
        <span>/ {props.lvl_3_spell_slots}</span>
      </div>
    </div>
  {/if}
  {#if props.lvl_4_spell_slots > 0}
    <div class="feat-stat middle">
      <strong>Level 4 Spell Slots:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={props.lvl_4_spell_slots}>
        <span>/ {props.lvl_4_spell_slots}</span>
      </div>
    </div>
  {/if}

  {#if props.rages > 0}
    <div class="feat-stat">
      <strong>Rage Uses:</strong>
      <div>
        <input class="xp-input" type="number" autocomplete="off"
          value={props.rages}>
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
          value={props.second_wind}>
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
