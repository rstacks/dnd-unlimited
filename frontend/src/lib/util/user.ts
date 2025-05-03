import { BACKEND_URL } from "$env/static/private";
import { error } from "@sveltejs/kit";
import bcrypt from "bcrypt";

interface UserInfo {
  id: number;
  phone_hash: string;
  session_uuid: string;
}

interface UsersJSON {
  users: UserInfo[];
}

export async function fetchUsers(): Promise<UserInfo[]> {
  const resp = await fetch(BACKEND_URL + "/users");
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
  const usersJson: UsersJSON = await resp.json();
  const allUsers = usersJson.users;
  return allUsers;
}

export async function getUserIdByPhone(phonePlaintext: string): Promise<number> {
  const allUsers = await fetchUsers();
  for (const user of allUsers) {
    const nextPhoneHash = user.phone_hash;
    const userExists = await bcrypt.compare(phonePlaintext, nextPhoneHash);
    if (userExists) {
      return user.id;
    }
  }
  return -1;
}

export async function getUserIdBySession(sessionId: string): Promise<number> {
  const allUsers = await fetchUsers();
  for (const user of allUsers) {
    const nextSessionId = user.session_uuid;
    if (sessionId === nextSessionId) {
      return user.id;
    }
  }
  return -1;
}
