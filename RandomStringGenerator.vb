Imports System
Imports System.Text.RegularExpressions

Module RandomStringGenerator

    Sub Main()
        Dim digits As String = "0123456789"
        Dim letters As String = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Dim allChars As String = digits & letters

        Dim rng As New Random()
        Dim result As String

        Do
            result = ""
            For i As Integer = 1 To 5
                Dim index As Integer = rng.Next(allChars.Length)
                result &= allChars(index)
            Next

            ' Validate: must contain at least one digit AND at least one letter
        Loop Until Regex.IsMatch(result, "[0-9]") AndAlso Regex.IsMatch(result, "[a-zA-Z]")

        Console.WriteLine(result)
    End Sub

End Module
