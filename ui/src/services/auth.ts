const JWT_TOKEN = process.env.REACT_APP_JWT_TOKEN;

export const authService = {
  isAuthenticated(): boolean {
    return !!JWT_TOKEN;
  },

  getToken(): string | null {
    return JWT_TOKEN || null;
  }
}; 