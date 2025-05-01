import type { PageServerLoad, Actions } from './$types';

// Will eventually need to load session IDs, I imagine
export const load = (async () => {
  return {};
}) satisfies PageServerLoad;

export const actions = {
  login: async ({ cookies, request }) => {
    // TODO: perform login
    console.log("Attempt login");
  },
  register: async ({ cookies, request }) => {
    // TODO: perform register
    console.log("Attempt register");
  }
} satisfies Actions;
