<script lang="ts">
  import { getAbilityModifier } from "$lib/util/character-functions";

  interface Props {
    hit_dice: string;
    lvl: number;
    dex: number;
    armor_class: number;
    hp: number;
    max_hp: number;
    notes: string;
    status_effects: string;
    proficiency_bonus: number;
    speed: number;
  }

  let props: Props = $props();
</script>

<section>
  <div>
    <strong>Background Info</strong>
    <textarea placeholder="Background Info (Optional)" value={props.notes}></textarea>
  </div>
  <div>
    <div>
      <strong>Initiative</strong>
      <span>
        {#if getAbilityModifier(props.dex) >= 0}
          +{getAbilityModifier(props.dex)}
        {:else}
          {getAbilityModifier(props.dex)}
        {/if}
      </span>
    </div>
  
    <div>
      <strong>Hit Dice</strong>
      <span>{props.lvl}{props.hit_dice}</span>
    </div>
  
    <div>
      <strong>Armor Class</strong>
      <span>{props.armor_class}</span>
    </div>
  
    <div>
      <strong>Hit Points</strong>
      <input class="numeric-input" type="number" autocomplete="off"
        value={props.hp}>
      <span>
        / {props.max_hp} HP
      </span>
    </div>
  </div>
  <div>
    <div>
      <strong>Proficiency Bonus</strong>
      <span>+{props.proficiency_bonus}</span>
    </div>
    <div>
      <strong>Speed</strong>
      <span>{props.speed} ft</span>
    </div>
  </div>
  <div>
    <strong>Status Effects</strong>
    <textarea placeholder="Status Effects" value={props.status_effects}></textarea>
  </div>
</section>

<style>
  textarea {
    resize: vertical;
  }

  .numeric-input {
    width: 6em;
  }
</style>
