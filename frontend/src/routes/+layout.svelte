<script lang="ts">
  import "../global.css";
  import Loading from "$lib/components/Loading.svelte";
  import { navigating } from "$app/state";

	let { children } = $props();
</script>

{#if navigating.to}
  <Loading />
{/if}

{@render children()}
