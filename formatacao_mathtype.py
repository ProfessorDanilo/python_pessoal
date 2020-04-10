from pyautogui import *
from time import sleep
from pynput import mouse




##### atualizado pela última vez em 24/01/2020

#hotkey('winleft', 'down')
#hotkey("shift", "f10")
#typewrite("j")
#typewrite("o")
#sleep(0.1)

#################################################################################
#################################################################################
#################################################################################
#Lembre-se de criar um macro cujo atalho é ctrl + y para abrir o mathtype
#Sub mathFormat()
#'
#' mathFormat Macro
#'
#'
# Selection.GoTo What:=wdGoToEquation, Which:=wdGoToNext, Count:=1, Name:=""
#    Selection.Find.ClearFormatting
#    Selection.Find.Replacement.ClearFormatting
#    With Selection.Find
#        .Text = " "
#        .Replacement.Text = " "
#        .Forward = True
#        .Wrap = wdFindContinue
#        .Format = False
#        .MatchCase = False
#        .MatchWholeWord = False
#        .MatchWildcards = False
#        .MatchSoundsLike = False
#        .MatchAllWordForms = False
#    End With
#    Selection.MoveRight Unit:=wdCharacter, Count:=1, Extend:=wdExtend
#    Selection.InlineShapes(1).OLEFormat.DoVerb VerbIndex:=wdOLEVerbPrimary
#End Sub
#################################################################################
#################################################################################
#################################################################################



#################################################################################
#################################################################################
#################################################################################
#Criar outra macro para formatação geral do word cujo atalho é ctrl + shift + B
#
#'
#' Macro1 Macro
#'
#'
#    Selection.Find.ClearFormatting
#    Selection.Find.Replacement.ClearFormatting
#    With Selection.Find
#        .Text = "  "
#        .Replacement.Text = " "
#        .Forward = True
#        .Wrap = wdFindContinue
#        .Format = False
#        .MatchCase = False
#        .MatchWholeWord = False
#        .MatchWildcards = False
#        .MatchSoundsLike = False
#        .MatchAllWordForms = False
#    End With
#    Selection.Find.Execute Replace:=wdReplaceAll
#    Selection.Find.Execute Replace:=wdReplaceAll
#    Selection.Find.Execute Replace:=wdReplaceAll
#    With Selection.Find
#        .Text = " ^p"
#        .Replacement.Text = "^p"
#        .Forward = True
#        .Wrap = wdFindContinue
#        .Format = False
#        .MatchCase = False
#        .MatchWholeWord = False
#        .MatchWildcards = False
#        .MatchSoundsLike = False
#        .MatchAllWordForms = False
#    End With
#    Selection.Find.Execute Replace:=wdReplaceAll
#    Selection.Find.Execute Replace:=wdReplaceAll
#    With Selection.Find
#        .Text = "ta:^p^p["
#        .Replacement.Text = "ta: "
#        .Forward = True
#        .Wrap = wdFindContinue
#        .Format = False
#        .MatchCase = False
#        .MatchWholeWord = False
#        .MatchWildcards = False
#        .MatchSoundsLike = False
#        .MatchAllWordForms = False
#    End With
#    Selection.Find.Execute Replace:=wdReplaceAll
#    With Selection.Find
#        .Text = "]^p^p"
#        .Replacement.Text = "^p"
#        .Forward = True
#        .Wrap = wdFindContinue
#        .Format = False
#        .MatchCase = False
#        .MatchWholeWord = False
#        .MatchWildcards = False
#        .MatchSoundsLike = False
#        .MatchAllWordForms = False
#    End With
#    Selection.Find.Execute Replace:=wdReplaceAll
#    Selection.WholeStory
#    With Selection.ParagraphFormat
#        .LeftIndent = CentimetersToPoints(0)
#        .RightIndent = CentimetersToPoints(0)
#        .SpaceBefore = 0
#        .SpaceBeforeAuto = False
#        .SpaceAfter = 0
#        .SpaceAfterAuto = False
#        .LineSpacingRule = wdLineSpaceSingle
#        .Alignment = wdAlignParagraphJustify
#        .FirstLineIndent = CentimetersToPoints(0)
#        .OutlineLevel = wdOutlineLevelBodyText
#        .CharacterUnitLeftIndent = 0
#        .CharacterUnitRightIndent = 0
#        .CharacterUnitFirstLineIndent = 0
#        .LineUnitBefore = 0
#        .LineUnitAfter = 0
#        .MirrorIndents = True
#    End With
#    Selection.MoveLeft Unit:=wdCharacter, Count:=1
#End Sub
#################################################################################
#################################################################################
#################################################################################

print("Para interromper o programa, tecle F")
print("Digite quantas vezes quer que seja repetida macro:")
#print("Para interromper o programa, mova o mouse","","Digite quantas vezes quer que seja repetida macro:")
n=int(input())
i=1
##hotkey("winleft", "down")
##for j in range(10):
##    print(j)
##    sleep(1)
##    if j==5:
##        hotkey("winleft", "down")

t=0.85
sleep(t)
hotkey('winleft', 'down')
sleep(t)
hotkey('winleft', 'down')
t=0.2
#hotkey("ctrl", "shift", "b")
#sleep(10*t)
while i<n:
    #atalho para acessar a equação
    hotkey("ctrl", "y")
    #formatar a equação
    keyDown('alt')
    sleep(t)
    typewrite("p")
    sleep(t)
    keyUp('alt')
    sleep(t)
    typewrite("1")
    sleep(t)
    press("enter")
    sleep(t)
    #centralizar o mathtype
    hotkey("ctrl", "a")
    hotkey("ctrl", "shift", "j")
    sleep(t)
    #fechar o mathtype
    hotkey("ctrl", "f4")
    i+=1
    sleep(t)
##    if press("F"):
##        break
##    if mouse.Events():
##        break
hotkey("ctrl", "b")
sleep(t)
if i==n:
    sleep(1)
##    hotkey('alt','f4')
    
#hotkey('altleft', 'q')

