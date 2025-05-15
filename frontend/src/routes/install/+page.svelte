<svelte:head>
  <title>Install App | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import Title from "$lib/components/Title.svelte";
</script>

<Title />

<article class="card">
  <div>
    <p>
      Greetings, iOS user! DnD Unlimited works best on your device
      as a <strong>standalone app</strong>. Here is how to install the DnD Unlimited app:
    </p>

    <ol>
      <li class="share-step">
        Tap the Share buttom at the bottom of your screen. It looks something 
        like this:
      </li>
    </ol>
    <figure class="share-icon">
      <img src="ios-share-icon.svg" alt="Share button">
    </figure>
    <ol start="2">
      <li>
        Tap on the "Add to Home Screen" option.
      </li>
      <li>
        Tap the "Add" button in the upper-right corner.
      </li>
      <li>
        DnD Unlimited has now been added to your device's home screen! Tap
        on its icon to launch the app.
      </li>
    </ol>

    <p>
      Safe travels, adventurer!
    </p>
  </div>
</article>

<div class="spacer"></div>

<style>
  article {
    margin-top: 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: left;
    max-width: 30em;
    width: 80%;
    margin: auto;
    padding: 1em;
  }

  figure.share-icon {
    display: flex;
    justify-content: center;
    margin: 0;
  }

  figure.share-icon img {
    width: 2em;
  }

  div.spacer {
    height: 2em;
  }
</style>
