<script lang="ts">
  // TODO: reset form inputs when close button pressed
  // function closeCharacterCreation(): void {
  //   const elem = document.getElementById("char-creation-screen");
  //   if (elem) {
  //     elem.style.display = "none";
  //   }
  // }
</script>
  
<article class="card" id="char-creation-screen">
  <header>
    <a class="back-button pseudo button" href="/dashboard">
      <img src="back-icon.svg" alt="Back to Dashboard Button">
    </a>
    <h3>Character Creation</h3>
  </header>
  <p>test</p>
</article>

<style>
  article {
    position: fixed;
    height: 100%;
    width: 100%;
    border-style: none;
    border-radius: 0;
  }

  header {
    display: flex;
    align-items: center;
  }

  .back-button {
    display: flex;
    padding: 0.25em;
    margin-right: 1em;
  }
</style>
  
  