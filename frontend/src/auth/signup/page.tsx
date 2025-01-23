import AuthForm from "@/components/auth-form"

export default function SignupPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-500 to-pink-500">
      <div className="w-full max-w-md">
        <AuthForm defaultTab="register" />
      </div>
    </div>
  )
}

