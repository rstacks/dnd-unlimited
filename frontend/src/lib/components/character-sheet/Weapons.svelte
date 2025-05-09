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

<div>
  <strong>Weapons</strong>
  {#each props.weapons as weapon}
    <div>
      <strong>Name</strong>
      <strong>Damage</strong>
      <span>{weapon.weapon_name}</span>
      <div>
        <span>{weapon.damage_die}</span>
        {#if weapon.weapon_type === "melee"}
          <span>{getAbilityModText(props.str)}</span>
        {:else if weapon.weapon_type === "ranged"}
          <span>{getAbilityModText(props.dex)}</span>
        {/if}
      </div>
    </div>
  {/each}
</div>

<div>
  <strong>Items</strong>
  {#if props.items.length === 0}
    <p>You don't have any items.</p>
  {/if}
  {#each props.items as item}
    <div>
      <strong>Name</strong>
      <strong>Amount</strong>
      <span>{item.item_name}</span>
      <span>{item.amount}</span>
    </div>
  {/each}
</div>
