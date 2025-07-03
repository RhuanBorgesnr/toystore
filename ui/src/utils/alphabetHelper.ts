export const findMissingLetter = (fullName: string): string => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const nameLower = fullName.toLowerCase();
  
  for (const letter of alphabet) {
    if (!nameLower.includes(letter)) {
      return letter.toUpperCase();
    }
  }
  
  return '-';
}; 