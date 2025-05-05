<!-- BIG THANKS FOR THE CLASS ICONS! https://www.flapkan.com/ -->

<article class="card">
  <header>
    <img src="class-icons/barbarian.svg" alt="Barbarian class icon" />
    <h4>Barbarian</h4>
  </header>
  <p><strong>Description:</strong> A wandering warrior imbued with primal magic.</p>
  <p><strong>Hit Dice:</strong> d8</p>
  <p>
    <strong>Feat:</strong> Spellcasting
    <label for="feat-modal" class="info-button pseudo button">
      <img src="info-icon.svg" alt="More feat info button">
    </label>
  </p>
  <p><strong>Save Proficiencies:</strong></p>
  <p><strong>Skill Proficiencies:</strong></p>
  <footer>
    <button>View Spells</button>
  </footer>
</article>

<div class="modal">
  <input type="checkbox" id="feat-modal">
  <label for="feat-modal" class="overlay"></label>
  <article>
    <header>
      <h3>Spellcasting</h3>
      <label for="feat-modal" class="close">&times;</label>
    </header>
    <section class="content">
      You have the ability to cast spells as an action. Depending on the class, you will have access to a specific set of cantrips and casted spells.\nCantrips are spells with no cost that can be cast as often as you desire.\nCasted spells consume a Spell Slot upon casting.\nYour character has a limited number of Spell Slots. As you gain levels, the number of Spell Slots available to you increases. You may also gain higher level Spell Slots.
    </section>
  </article>
</div>

<style>
  article {
    width: 20em;
    margin: auto;
    margin-top: 1em;
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
    font-size: 0.9em;
  }

  footer {
    padding-top: 0;
  }

  .info-button {
    padding: 0;
  }

  .modal section {
    padding-bottom: 1em;
  }
</style>
