export const LEVEL_TO_XP_MIN = {
  1: 0,
  2: 300,
  3: 900,
  4: 2700,
  5: 6500,
  6: 14000,
  7: 23000,
  8: 34000,
  9: 48000,
  10: 64000,
  11: 85000,
  12: 100000,
  13: 120000,
  14: 140000,
  15: 165000,
  16: 195000,
  17: 225000,
  18: 265000,
  19: 305000,
  20: 355000
};

export function getAbilityModifier(abilityScore: number): number {
  return Math.floor((abilityScore - 10) / 2);
}

export function getAbilityModText(abilityScore: number): string {
  const mod = getAbilityModifier(abilityScore);
  if (mod >= 0) {
    return "+" + mod.toFixed(0);
  }
  return mod.toFixed(0);
}
