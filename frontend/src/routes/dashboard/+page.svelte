<svelte:head>
  <title>Dashboard | DnD Unlimited</title>
</svelte:head>

<script lang="ts">
  import TitleBar from "$lib/components/TitleBar.svelte";
  import type { PageProps } from "./$types";

  let { data }: PageProps = $props();
</script>

<TitleBar />

<h2>Welcome, {data.name}!</h2>
