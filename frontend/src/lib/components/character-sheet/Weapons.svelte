<script lang="ts">
  import { getAbilityModifier } from "$lib/util/character-functions";
  import type { Weapon, Item } from "$lib/util/character";

  interface Props {
    str: number;
    dex: number;
    weapons: Weapon[];
    items: Item[];
  }

  let props: Props = $props();

  function getAbilityModText(abilityScore: number): string {
    const mod = getAbilityModifier(abilityScore);
    if (mod >= 0) {
      return "+" + mod.toFixed(0);
    }
    return mod.toFixed(0);
  }
</script>

<div class="weapon-container">
  <strong>Weapons</strong>
  {#each props.weapons as weapon}
    <div class="weapon-info">
      <div class="weapon-name">
        <strong>Name</strong>
        <span>{weapon.weapon_name}</span>
      </div>
      <div class="weapon-dmg">
        <strong>Damage</strong>
        <div>
          <span>{weapon.damage_die}</span>
          {#if weapon.weapon_type === "melee"}
            <span>{getAbilityModText(props.str)}</span>
          {:else if weapon.weapon_type === "ranged"}
            <span>{getAbilityModText(props.dex)}</span>
          {/if}
        </div>
      </div>
    </div>
  {/each}
</div>

<div class="weapon-container bottom">
  <strong>Items</strong>
  {#if props.items.length === 0}
    <p>You don't have any items.</p>
  {/if}
  {#each props.items as item}
    <div class="weapon-info items">
      <div class="item-name">
        <strong>Name</strong>
        <span>{item.item_name}</span>
      </div>
      <div class="item-amount">
        <strong>Amount</strong>
        <span>{item.amount}</span>
      </div>
    </div>
  {/each}
</div>

<style>
  .weapon-container {
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

  .weapon-info {
    background-color: rgb(196, 230, 242);
    border-radius: 0.5em;
    width: fit-content;
    margin: auto;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    display: flex;
    justify-content: center;
    padding: 1em;
    padding-top: 0.5em;
    padding-bottom: 0.5em;
  }

  .weapon-name {
    display: flex;
    flex-direction: column;
    width: 10em;
  }

  .weapon-dmg {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    text-align: center;
  }

  .items div {
    display: flex;
    flex-direction: column;
  }

  .item-name {
    width: 10em;
  }

  .item-amount {
    text-align: center;
    flex-grow: 1;
  }

  .bottom {
    margin-bottom: 1em;
  }
</style>
