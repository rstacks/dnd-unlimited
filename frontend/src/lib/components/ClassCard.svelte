<!-- BIG THANKS FOR THE CLASS ICONS! https://www.flapkan.com/ -->

<script lang="ts">
  import type { ClassData } from "$lib/util/class";

  interface Props {
    classData: ClassData;
    allClasses: ClassData[];
    selected: boolean;
  }

  let { classData, allClasses, selected }: Props = $props();
</script>

<article class="card class-card"
  style:background-color="{selected ? "rgb(196, 230, 242)" : "white"}">
  <header>
    <img src="{"class-icons/" + classData.class_name.toLowerCase() + ".svg"}"
      alt="Barbarian class icon" />
    <h4>{classData.class_name}</h4>
  </header>
  <p><strong>Description:</strong> {classData.class_desc}</p>
  <p><strong>Hit Dice:</strong> {classData.hit_dice}</p>
  <p class="feat-info">
    <strong>Feat:</strong> {classData.feat_name}
    <label for="{"feat-modal-" + classData.id}" class="info-button pseudo button">
      <img src="info-icon.svg" alt="More feat info button">
    </label>
  </p>
  <p>
    <strong>Save Proficiencies:</strong>
    {#each classData.saves as save, i}
      {#if i === 0}
        {save}
      {:else}
        , {save}
      {/if}
    {/each}
  </p>
  <p>
    <strong>Skill Proficiencies:</strong>
    {#each classData.skills as skill, i}
      {#if i === 0}
        {skill}
      {:else}
        , {skill}
      {/if}
    {/each}    
  </p>
  {#if classData.feat_name.toLowerCase() === "spellcasting"}
    <footer>
      <button tabindex="-1">View Spells</button>
    </footer>
  {/if}
</article>

{#each allClasses as classRecord}
  <div class="modal">
    <input type="checkbox" id="{"feat-modal-" + classRecord.id}">
    <label for="{"feat-modal-" + classRecord.id}" class="overlay"></label>
    <article>
      <header>
        <h3>{classRecord.feat_name}</h3>
        <label for="{"feat-modal-" + classRecord.id}" class="close">&times;</label>
      </header>
      <section class="content">
        {#each classRecord.feat_desc as chr}
          {#if chr === "\n"}<br><br>{:else if chr === "-"}&#x2022;{:else}{chr}{/if}
        {/each}
      </section>
    </article>
  </div>
{/each}

<style>
  .class-card {
    width: 15em;
    margin: auto;
    margin-top: 1em;
    margin-bottom: 1em;
  }

  header {
    display: flex;
    align-items: center;
  }

  header img {
    max-width: 2em;
  }

  header h4 {
    margin: 0;
    margin-left: 0.5em;
  }

  article p {
    font-size: 0.8em;
  }

  footer {
    padding-top: 0;
  }

  .info-button {
    padding: 0;
    margin-left: 0.2em;
  }

  .feat-info {
    display: flex;
    align-items: center;
  }

  .feat-info strong {
    margin-right: 0.3em;
  }

  .modal section {
    padding-bottom: 1em;
  }

  .modal {
    font-size: 0.8em;
  }
</style>
