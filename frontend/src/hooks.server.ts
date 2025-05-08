import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
  if (event.url.pathname.startsWith("/character-creation")) {
    return await resolve(event, {
      transformPageChunk: ({ html, done }) => {
        if (!done) {
          return html.replace(
            '<body>',
            '<body><p class="card" style="width: fit-content; padding: 0.25em; margin: auto; margin-top: 1em;">Loading...</p></body>'
          );
        }
        return html;
      }
    });
  }

  return await resolve(event);
};
