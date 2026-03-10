#!/usr/bin/env elixir
defmodule Lorem2 do
  @nouns [
    "bagoly", "paprika", "erdő", "papucs", "villanykacsa", "tornádó", "kürtőskalács",
    "torta", "fánk", "hidrogén", "buborék", "szendvics", "tükör", "szék", "asztal",
    "bicikli", "macska", "kutya", "telefon", "szivárvány", "cseresznye", "szőlő",
    "zebra", "póló", "kalap", "cipő", "szomszéd", "robogó", "porszívó"
  ]
  @adjectives [
    "kockás", "sárga", "csintalan", "békés", "zajos", "szomorú", "vidám", "ragacsos",
    "cukros", "fűszeres", "parázsló", "színes", "hűvös", "furfangos", "szagos"
  ]
  @verbs [
    "fut", "táncol", "suttog", "sikolyog", "szalad", "pattog", "kecmereg", "szendereg",
    "forog", "dübörög", "mormol", "csoszog", "teker", "gurul"
  ]
  @objects [
    "szandál", "kalap", "kürtő", "csoki", "szendvics", "paplan", "csiga", "hinta",
    "lámpa", "sátor", "festék", "ceruza"
  ]
  @adverbs [
    "furcsán", "halkan", "vidáman", "búsan", "pörgősen", "lassan", "hangosan", "büszkén"
  ]
  @places [
    "szigeten", "erdőben", "utcán", "piacon", "múzeumban", "kávéházban", "szobában"
  ]

  @vowels ~w(a á e é i í o ó ö ő u ú ü ű)

  @patterns [
    [:adj, :noun, :verb, :place],
    [:noun, :verb, :object],
    [:adj, :noun, :adv, :verb, :object, :place],
    [:noun, :adv, :verb, :object],
    [:adj, :noun, :verb]
  ]

  def article_for(word) do
    first = word |> String.downcase() |> String.first()
    if first in @vowels, do: "az", else: "a"
  end

  def random(:noun),   do: Enum.random(@nouns)
  def random(:adj),    do: Enum.random(@adjectives)
  def random(:verb),   do: Enum.random(@verbs)
  def random(:object), do: Enum.random(@objects)
  def random(:adv),    do: Enum.random(@adverbs)
  def random(:place),  do: Enum.random(@places)

  def make_sentence do
    pattern = Enum.random(@patterns)
    tokens = Enum.map(pattern, fn t -> {t, random(t)} end)
    words = build_words(tokens, [])

    case words do
      [] -> "Semmi."
      [first | rest] ->
        capitalized = String.upcase(String.first(first)) <> String.slice(first, 1..-1//1)
        Enum.join([capitalized | rest], " ") <> "."
    end
  end

  # Build word list: when ADJ is followed by NOUN, insert article before adj+noun
  defp build_words([], acc), do: Enum.reverse(acc)

  defp build_words([{:adj, adj}, {:noun, noun} | rest], acc) do
    art = article_for(adj)
    build_words(rest, [noun, adj, art | acc])
  end

  defp build_words([{:noun, noun} | rest], acc) do
    art = article_for(noun)
    build_words(rest, [noun, art | acc])
  end

  defp build_words([{:object, obj} | rest], acc) do
    art = article_for(obj)
    build_words(rest, [obj, art | acc])
  end

  defp build_words([{_type, word} | rest], acc) do
    build_words(rest, [word | acc])
  end

  def main do
    n =
      case IO.gets("Hány mondatot akarsz? ") do
        :eof ->
          IO.puts("\nKilépés.")
          System.halt(0)

        input ->
          input
          |> String.trim()
          |> Integer.parse()
          |> case do
            {count, _} when count >= 1 -> count
            _ -> 1
          end
      end

    Enum.each(1..n, fn _ -> IO.puts(make_sentence()) end)
  end
end

Lorem2.main()
